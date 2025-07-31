# helpers.py
# Build a normalized profile dict from raw form inputs
"""
        Convert raw form data (strings) into canonical tags matching the DB columns.

        Expects form to have keys:
        - height (cm)
        - weight (kg)
        - arm_strength (Low/Medium/High)
        - playing_style (one of our tags)
        - preferred_balance (Power/Control/Balanced)
        - comfort_priority (yes/no)
        - string_preference (Power/Spin/Control/Durability)
        - skill_level (Beginner/Intermediate/Advanced)

        Returns a dict with keys:
        - skill_level           (string)
        - playing_style         (string)
        - arm_strength          (string)
        - preferred_balance     (string)
        - comfort_priority      ("Yes" or "No")
        - string_preference     (string)
        - string_preference (str)
        - height_cm         (int)  — users exact height in cm
        - weight_kg         (int)  — users exact weight in kg
    """

def build_profile(form):
    h = float(form.get('height', 0))
    w = float(form.get('weight', 0))

    def bucket_height(cm):
        if cm < 165:   return '150-165 cm'
        elif cm < 180: return '165-180 cm'
        else:          return '180+ cm'

    def bucket_weight(kg):
        if kg < 70:    return '50-70 kg'
        elif kg < 90:  return '70-90 kg'
        else:          return '90+ kg'

    return {
        'skill_level':       form.get('skill_level', '').strip().lower(),
        'playing_style':     form.get('playing_style', '').strip().lower(),
        'arm_strength':      form.get('arm_strength', '').strip().lower(),
        'preferred_balance': form.get('preferred_balance', '').strip().lower(),
        'string_preference': form.get('string_preference', '').strip().lower(),
        'height_cm':         h,
        'weight_kg':         w,
        'height_bucket':     bucket_height(h),
        'weight_bucket':     bucket_weight(w),
    } 


