# match.py
import sqlite3, re

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
    try:
        field = r['strung_weight']
    except KeyError:
        return None
    if not field:
        return None
    m = re.search(r'(\d+(?:\.\d+)?)', field)
    return float(m.group(1)) if m else None

def normalize_tags(tag_str):
    return [t.strip().lower() for t in str(tag_str).split(',') if t.strip()]

def in_user_ranges(rw, user_w, user_h):
    if not rw: return False
    if user_w < 70:
        return rw < 295
    elif user_w < 90:
        return 280 <= rw <= 315
    else:
        return rw >= 300

def match_racquets(profile, top_n=6):
    conn = _connect()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Don't filter — fetch all racquets
    c.execute("SELECT * FROM racquets")
    rows = c.fetchall()
    conn.close()

    scored = []
    for rac in rows:
        score = 0
        rw = get_strung_weight_g(rac)

        # Score tag matches
        for col in TAG_COLUMNS:
            profile_val = profile[col]
            rac_tags = normalize_tags(rac[col])
            if profile_val in rac_tags:
                score += 1

        #  Smart weight match adds to score
        if in_user_ranges(rw, profile['weight_kg'], profile['height_cm']):
            score += 1

        scored.append((score, dict(rac)))

    # Sort: higher score first, then lower price
    scored.sort(key=lambda x: (-x[0], float(x[1].get('price', 9999))))

    # Always return top N matches, even if score is 0
    return [r for _, r in scored[:top_n]]







