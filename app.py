from flask import Flask, render_template, request, redirect, url_for
from helpers import build_profile
from match import match_racquets
import os

app = Flask(__name__)

# Reload templates on each request (for development)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

@app.route('/')
def index():
    """
    Landing page: Full-screen hero section.
    """
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form():
    """
    Form page: User selects skill/style/strength/etc.
    """
    fields = [
        {"name": "skill_level", "label": "Skill Level", "options": ["Beginner", "Intermediate", "Advanced"]},
        {"name": "playing_style", "label": "Playing Style", "options": [
            "Baseline Aggressive", "Baseline Defensive", "All-Court", "Net Attacker", "Counterpuncher",
            "Power Player", "Spin Specialist", "Doubles Specialist", "Recreational", "Control Player"
        ]},
        {"name": "arm_strength", "label": "Arm Strength", "options": ["Low", "Medium", "High"]},
        {"name": "preferred_balance", "label": "Preferred Balance", "options": ["Power", "Control", "Balanced"]},
        {"name": "string_preference", "label": "String Preference", "options": ["Power", "Spin", "Control", "Durability"]}
    ]
    return render_template('form.html', fields=fields)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    """
    Handle form submission and show racquet matches.
    Redirects GET requests back to the form.
    """
    if request.method == 'GET':
        return redirect(url_for('form'))

    profile = build_profile(request.form)
    matches = match_racquets(profile, top_n=6)
    no_matches = len(matches) == 0

    return render_template('results.html', racquets=matches, profile=profile, no_matches=no_matches)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
