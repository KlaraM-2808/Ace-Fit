AceFit — Tennis Racquet Recommendation System

A full-stack application that delivers personalized racquet recommendations using structured racquet specifications, player profiling, and a modular scoring algorithm.

1. Purpose

AceFit was designed to solve a practical problem encountered in real tennis coaching: players often choose racquets without understanding how weight, balance, head size, stiffness, and other technical characteristics affect their performance.

This project demonstrates your ability to:

Identify a real-world problem

Analyze its constraints

Translate domain expertise into engineering logic

Build a complete technical solution end-to-end

AceFit combines scraped product data, a relational database, a scoring engine, and a Flask backend to produce accurate and consistent recommendations.

2. Key Features

Structured database of real racquet specifications

Scoring algorithm based on player physical profile and play characteristics

Clean separation between data, logic, and presentation

Modular codebase allowing expansion (new racquets, new scoring layers)

Simple UI for input and interpretation

Lightweight and fast architecture for local or cloud deployment

3. Architecture Overview
acefit/
├── app.py                     # Flask routes and recommendation processing
│
├── scraper/
│   └── scrape.py              # Scrapes racquet data and populates SQLite DB
│
├── templates/
│   ├── index.html             # Player input form
│   └── results.html           # Recommendations output page
│
├── static/
│   ├── styles.css
│   └── images/
│
├── racquets.db                # Normalized racquet dataset
└── requirements.txt           # Project dependencies


Backend:

Flask handles input validation, routing, and output rendering

Algorithm functions are isolated for clarity and testability

Data:

SQLite used for simplicity, reliability, and portability

Scraper generates consistent, structured racquet data

Frontend:

Jinja templates provide lightweight server-rendered pages

4. Data Model

The database contains a single normalized racquet table.

racquets

Column	Type	Description
id	INTEGER	Primary key
brand	TEXT	Manufacturer
model	TEXT	Racquet model
head_size	INTEGER	Head size (sq in)
weight	INTEGER	Unstrung or equivalent weight
balance	TEXT	Balance point (e.g., HL, HH)
stiffness	INTEGER	RA stiffness rating
string_pattern	TEXT	Example: 16x19, 18x20
price	REAL	Retail price

The dataset is generated via scrape.py, which extracts specifications from a trusted source and ensures uniform formatting.

5. Recommendation Algorithm
Step 1 — Input Processing

The player’s profile is captured through:

Height

Weight

Skill Level

Play Style preferences (e.g., more power vs more control)

Step 2 — Filtering Layer

Racquets are filtered using thresholds based on:

Weight range

Head size

Balance category

Stiffness (comfort vs performance)

Step 3 — Scoring Layer

Each racquet is scored according to:

Maneuverability

Stability

Power potential

Control potential

Player compatibility

Scores are adjustable via a weighting system to support tuning or expansion.

Step 4 — Ranking

Racquets are sorted in descending order and displayed in the results view.

6. Installation & Local Setup
Clone the repository
git clone https://github.com/YOUR_USERNAME/acefit.git
cd acefit

Set up virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Run the server
flask run


The application runs at:
http://127.0.0.1:5000/

7. Engineering Considerations

A professional engineering environment would benefit from:

Separation of concerns:
Algorithm logic, scraping, and app routing are isolated for clarity and maintainability.

Data normalization:
Ensures consistent querying, filtering, and scoring.

Deterministic output:
Given the same inputs and dataset, the algorithm always yields consistent recommendations, which is important for testing and QA.

Easy migration:
Codebase is intentionally structured to be rebuilt as a TypeScript / Node backend in the future.

8. Future Improvements
Backend

Rebuild backend using TypeScript (Node + Express)

Add automated tests for recommendation functions

Implement caching to reduce repeated scoring operations

Introduce a configuration layer for algorithm weight tuning

Frontend

Modern client UI (React, Next.js, or Svelte)

More granular input steps for better user clarity

Data

Expand dataset to include additional brands and pro models

Add metadata (comfort indexes, swingweight, spin potential)

Provide administrative tools for updating the racquet database

Deployment

Deploy to Render, Railway, or AWS

Add logs, monitoring and metrics

9. What This Project Demonstrates

AceFit highlights capabilities relevant to a professional engineering environment:

Backend development using Flask

Database design and interaction

Data ingestion via scraping and cleaning

Algorithmic thinking and scoring logic

Practical application of domain knowledge

Ability to deliver a functioning, complete system

Clean code organization and maintainable structure

Incremental thinking and clear future expansion pathways

10. Author

Klara Milojkovic Trout
Software Developer & Tennis Professional

Author

Klara Milojkovic Trout
Software Developer & Tennis Professional
