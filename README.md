AceFit — Tennis Racquet Recommendation System

A data-driven recommendation engine built with Python, Flask, and a structured racquet dataset.

Overview

AceFit is a full-stack web application that recommends tennis racquets based on a player’s physical profile and playing characteristics. It uses real product data scraped from Tennis Warehouse, normalized into a SQLite database, and processed through a custom matching algorithm.

This project originated from a real coaching need: players typically select racquets without understanding which specifications match their game. AceFit provides personalized, structured recommendations using a reproducible logic model.

Tech Stack
Backend

Python (Flask) – routing, form processing, recommendation logic

SQLite – relational database for racquet specifications

BeautifulSoup – scraping and data extraction

Custom scoring and filtering algorithm

Frontend

HTML, CSS, Bootstrap

Jinja templates for server-rendered views

Project Structure


acefit/
├── app.py                     # Flask routes and recommendation processing
│
├── scraper/
│   └── scrape.py              # Scrapes racquet data and populates SQLite DB
│
├── templates/
│   ├── index.html             # Player input form
│   └── results.html           # Results page with recommended racquets
│
├── static/
│   ├── styles.css
│   └── images/
│
├── racquets.db                # Normalized racquet dataset
└── requirements.txt


Recommendation Algorithm
1. Input Collection

User inputs:

Height

Weight

Skill level

Playing style characteristics (power, control, etc.)

2. Filtering Layer

Initial filtering based on:

Weight range

Head size

Balance category

Stiffness

3. Scoring Layer

Each racquet is assigned weighted scores according to:

Maneuverability

Stability

Power potential

Control potential

Comfort

Compatibility with user’s profile

4. Ranking

Racquets are ordered by final composite score and displayed in the results template.

Database

The SQLite database contains a normalized dataset of racquet specifications.

Table: racquets

Column	Type	Description
id	INTEGER	Primary key
brand	TEXT	Manufacturer
model	TEXT	Model name
head_size	INTEGER	Head size (sq in)
weight	INTEGER	Weight (g)
balance	TEXT	Balance category
stiffness	INTEGER	RA stiffness rating
string_pattern	TEXT	16x19, 18x20, etc.
price	REAL	Retail price

Population of this table is handled by scrape.py.

Running AceFit Locally
1. Clone
git clone https://github.com/YOUR_USERNAME/acefit.git
cd acefit

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask application
flask run


Application is available at:
http://127.0.0.1:5000/

Features

Player-specific racquet recommendations

Real racquet specifications and technical attributes

Structured scoring algorithm

Clean, lightweight backend

Simple and direct UI built for rapid inputs and interpretation

Modular architecture that supports future expansion

Future Improvements
Backend

Rebuild application as a TypeScript Node.js API

Add unit tests for scoring logic

Introduce a caching layer for faster responses

Implement authentication for saving profiles

Frontend

Modernize UI using React or Next.js

Add multi-step form for improved input clarity

Data and Algorithm

Expand dataset with more racquets and custom tags

Add machine learning model for predictive scoring

Introduce comfort/injury risk scoring

Build an admin interface for updating the racquet dataset

Deployment

Deploy to Render, Railway, or AWS

Add uptime and performance monitoring

What This Project Demonstrates

Ability to build an end-to-end full-stack application

Database design and normalization

Data scraping and preprocessing

Backend architecture and route design

Practical algorithm design

Clean project structure and maintainable code

Ability to turn domain expertise (tennis coaching) into functional engineering solutions

Author

Klara Milojkovic Trout
Software Developer & Tennis Professional
