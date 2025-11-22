Ace Fit: Personalized Tennis Racquet Recommendation Tool
Ace Fit is a lightweight web application that recommends tennis racquets based on player profile inputs (height, weight, skill level, playing style, and power/control preference).
 The goal of the project is to translate real-world coaching logic into a simple, structured recommendation engine using accessible tools and clean data.

Purpose
Selecting a racquet is often confusing for players who don’t understand technical specifications like head size, balance, or swingweight.
 Ace Fit provides a focused, rule-based system that maps player characteristics to appropriate racquet attributes.
This project demonstrates:
practical use of Python for backend logic


web scraping and structured data storage


clean separation of responsibilities (scraper → database → algorithm → UI)


straightforward user-facing functionality


an approach to modeling real-world decision rules in code



Technical Overview
Backend:
Python (Flask)


SQLite for local data persistence


BeautifulSoup for scraping racquet specs


Recommendation logic implemented as a deterministic rule-based model


Frontend:
HTML/CSS


Bootstrap for layout and responsive design


Key Concepts Demonstrated:
Data acquisition and normalization


Lightweight API-style routing using Flask


Scoring logic based on mapped attributes


Database querying and result ranking


Clean project structure suitable for extension



Architecture
acefit/
│── app.py                 # Flask routes and recommendation processing
│── scraper/
│     └── scrape.py        # Scrapes racquet data and populates SQLite DB
│── templates/
│     ├── index.html       # Player input form
│     └── results.html     # Results page with structured output
│── static/
│     ├── styles.css
│     └── images/
│── racquets.db            # Normalized racquet dataset
└── requirements.txt


Recommendation Logic
The system applies a simple rules-engine approach:
Accept player attributes (physical profile, experience, preference).


Match them against racquet characteristics such as:


Weight


Balance


Head size


String pattern


Beam width


Compute a score for each racquet based on suitability.


Return the highest-ranked models with explanation fields.


This design makes it easy to extend, refactor, or convert to a more advanced model later.

Setup Instructions
git clone https://github.com/YOUR-USERNAME/acefit.git
cd acefit
python3 -m venv venv
source venv/bin/activate  # macOS
pip install -r requirements.txt
flask run


Potential Extensions
Convert to a TypeScript/React frontend


Deploy as a serverless API (AWS Lambda + API Gateway)


Replace rule-based logic with a small ML ranking model


Expand scraping to multiple sources


Add authentication and user profiles


Integrate a comparison view between recommended racquets



Author
Klara Milojkovic Trout
Tennis professional and junior software developer interested in backend development, cloud fundamentals, and full-stack web applications.
