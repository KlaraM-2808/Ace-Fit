AceFit — Tennis Racquet Recommendation System

AceFit is a lightweight web application that recommends tennis racquets based on a player’s height, weight, skill level, and playing characteristics.
It uses real racquet specifications scraped from Tennis Warehouse and stored in a structured SQLite database.

This project demonstrates practical backend skills: data ingestion, database design, routing, and algorithmic scoring.

Project Structure

The following version WILL format correctly in GitHub.
Copy and paste it exactly as-is (without modifying anything):


acefit/
├── app.py                  # Flask routes and recommendation logic
│
├── scraper/
│   └── scrape.py           # Scrapes racquet data and loads it into SQLite
│
├── templates/
│   ├── index.html          # Input form
│   └── results.html        # Recommendation output
│
├── static/
│   ├── styles.css
│   └── images/
│
├── racquets.db             # Structured racquet dataset
└── requirements.txt



If it still collapses in your README after this, it means your code block is not opened/closed correctly, and I’ll fix that next.

How It Works (Short Version)

1. Input
User enters:

Height

Weight

Skill level

Play-style preferences

2. Filtering
Racquets are filtered by:

Weight range

Head size

Balance

Stiffness

3. Scoring
A scoring function ranks each racquet based on:

Maneuverability

Stability

Power

Control

Fit for the player’s profile

4. Output
Top recommendations are shown in the results page.

Running the App
git clone https://github.com/YOUR_USERNAME/acefit.git
cd acefit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run


Visit:
http://127.0.0.1:5000/

Tech Used

Python

Flask

SQLite

BeautifulSoup

HTML/CSS (Jinja templates)

Next Steps

Rewrite backend using TypeScript + Node.js

Add unit tests for scoring logic

Expand racquet dataset

Deploy to Render/Railway

Author

Klara Milojkovic Trout
