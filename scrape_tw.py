#scraping libraries= get data from website: requests= python / BeautifulSoup= python library allowing to pick specific filters from HTML
import requests 
from bs4 import BeautifulSoup

#database library - save data into racquets.db 
import sqlite3

BASE_URL = "https://www.tennis-warehouse.com"
BESTSELLERS_URL = "https://www.tennis-warehouse.com/Best_Selling_Tennis_Racquets/catpage-BSRACS.html" 
HEADERS = HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# ---- FUNCTIONS ----

def fetch_bestsellers_page():
    """request the bestseller page to get the list of racquets."""
    response = requests.get(BESTSELLERS_URL, headers=HEADERS)
    return BeautifulSoup(response.text, 'html.parser') 

def parse_racquet_links(soup):
    """parse and find all racquet links on the bestseller page."""
    # Find all <a> tags with class 'product' (adjust if needed)
    return soup.find_all('a', class__='product') 

"""STILL NEED TO MODIFY ALL NAMES FOR EACH FILTER FROM 'INSPECT'! """
def scrape_racquet_details(product_url):
    """Scrape individual racquet detail page."""
    response = requests.get(product_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract racquet name
    try:
        name = soup.find('h1', class_='h2 desc_top_head_title').get_text(strip=True)
    except:
        name = "Unknown Model"

    # Extract price
    try:
        price_text = soup.find('div', class_='afterpay-full_price').get_text(strip=True).replace("$", "")
        price = float(price_text.split()[0])
    except:
        price = 0.0

    # Extract head size
    try:
        head_size_text = soup.find('div', class_='REPLACE_WITH_HEADSIZE_CLASS').get_text(strip=True)
        head_size = int(head_size_text.replace(" sq. in.", ""))
    except:
        head_size = 0

    # Extract weight
    try:
        weight_text = soup.find('div', class_='REPLACE_WITH_WEIGHT_CLASS').get_text(strip=True)
        weight = int(weight_text.replace(" g", ""))
    except:
        weight = 0

    # Extract balance
    try:
        balance = soup.find('div', class_='REPLACE_WITH_BALANCE_CLASS').get_text(strip=True)
    except:
        balance = 'N/A'

    # Extract string pattern
    try:
        string_pattern = soup.find('div', class_='REPLACE_WITH_STRINGPATTERN_CLASS').get_text(strip=True)
    except:
        string_pattern = 'N/A'

    # Extract grip size
    try:
        grip_size = soup.find('div', class_='REPLACE_WITH_GRIPSIZE_CLASS').get_text(strip=True)
    except:
        grip_size = 'N/A'

    # Extract product info (e.g., description, highlights)
    try:
        product_info = soup.find('div', class_='REPLACE_WITH_PRODUCTINFO_CLASS').get_text(strip=True)
    except:
        product_info = 'No additional info'

    # Extract brand (assuming first word of the name)
    brand = name.split()[0] if name != "Unknown Model" else "Unknown"

    print(f"Scraping: {name} | Price: {price} | Link: {product_url}")

    # Return all fields
    return (brand, name, head_size, weight, balance, string_pattern, grip_size, price, product_url, product_info)


def save_racquet_to_db(cursor, racquet_data):
    """Insert racquet data into the database."""
    cursor.execute('''
        INSERT INTO racquets (brand, model, head_size, weight, balance, string_pattern, grip_size, price, link, product_info)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', racquet_data)

def main():
    """Main scraper flow."""
    # 1. Connect to your database
    conn = sqlite3.connect('racquets.db')
    c = conn.cursor()

    # 2. Scrape bestseller page & extract racquet links
    soup = fetch_bestsellers_page()
    racquet_links = parse_racquet_links(soup)

    # 3. Loop over racquet links and scrape each racquet
    for link in racquet_links:
        partial_url = link.get('href')
        product_url = BASE_URL + partial_url

        racquet_data = scrape_racquet_details(product_url)
        save_racquet_to_db(c, racquet_data)

    # 4. Save & close the database
    conn.commit()
    conn.close()

    print("Scraping complete!")

# -------- RUN PROGRAM --------
if __name__ == "__main__":
    main() 