# match.py
import sqlite3
import re

DB_PATH = 'racquets.db'

TAG_COLUMNS = [
    'skill_level',
    'playing_style',
    'arm_strength',
    'preferred_balance',
    'string_preference',
]

def _connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def get_strung_weight_g(r):
    """
    Extract numeric weight in grams from 'strung_weight' field.
    Example: '300 g' or '11.2oz / 318g' -> 300 or 318
    """
    try:
        field = r['strung_weight']
    except KeyError:
        return None
    if not field:
        return None
    m = re.search(r'(\d+(?:\.\d+)?)', field)
    return float(m.group(1)) if m else None

def normalize_tags(tag_str):
    """
    Split comma-separated tags into a list of lowercase values.
    """
    return [t.strip().lower() for t in str(tag_str).split(',') if t.strip()]

def in_user_ranges(rw, user_w, user_h):
    """
    Score based on racquet weight vs user body type.
    """
    if not rw:
        return False
    if user_w < 70:
        return rw < 295
    elif user_w < 90:
        return 280 <= rw <= 315
    else:
        return rw >= 300

def match_racquets(profile, top_n=6):
    """
    Matches racquets to user profile and returns top_n best ones.
    """
    conn = _connect()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM racquets")
    rows = c.fetchall()
    conn.close()

    scored = []
    for rac in rows:
        score = 0
        rw = get_strung_weight_g(rac)

        # Score based on tag similarity
        for col in TAG_COLUMNS:
            profile_val = profile[col]
            rac_tags = normalize_tags(rac[col])
            if profile_val in rac_tags:
                score += 1

        # Score for good weight match
        if in_user_ranges(rw, profile['weight_kg'], profile['height_cm']):
            score += 1

        rac_dict = dict(rac)

        # 🧼 Clean the link
        link = rac_dict.get("link", "").strip().strip("',\"")
        if link and not link.startswith("http"):
            link = "https://www.tennis-warehouse.com" + link
        rac_dict["link"] = link

        scored.append((score, rac_dict))

    # Sort: higher score first, then lower price
    scored.sort(key=lambda x: (-x[0], float(x[1].get('price', 9999))))

    # 🧪 Debug: print top link URLs
    for _, racquet in scored[:top_n]:
        print("Racquet link:", racquet.get("link"))

    return [r for _, r in scored[:top_n]]
