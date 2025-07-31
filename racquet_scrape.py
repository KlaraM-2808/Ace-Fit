import requests
from bs4 import BeautifulSoup
import csv
import os 

# List of racquet URLs
urls = [
    'https://www.tennis-warehouse.com/Babolat_Pure_Aero_2023/descpageRCBAB-BARO.html',
    'https://www.tennis-warehouse.com/Babolat_Pure_Aero_98_2023/descpageRCBAB-BARO98.html',
    'https://www.tennis-warehouse.com/Babolat_Pure_Drive_2025/descpageRCBAB-BPD25R.html',
    'https://www.tennis-warehouse.com/Babolat_Pure_Drive_98_2025/descpageRCBAB-PD98R.html',
    'https://www.tennis-warehouse.com/Babolat_Pure_Strike_100/descpageRCBAB-STRPS.html',
    'https://www.tennis-warehouse.com/Babolat_Pure_Strike_98_16x19/descpageRCBAB-PSRKT.html',
    'https://www.tennis-warehouse.com/Head_Speed_Pro/descpageRCHEAD-SPDP.html',
    'https://www.tennis-warehouse.com/Head_Gravity_Tour_2025/descpageRCHEAD-HGTRR.html',
    'https://www.tennis-warehouse.com/Head_Gravity_Pro_2025/descpageRCHEAD-HGPRR.html',
    'https://www.tennis-warehouse.com/Head_Radical_MP_2021/descpageRCHEAD-HRRMP.html',
    'https://www.tennis-warehouse.com/Head_Radical_MP_2023/descpageRCHEAD-HMPR.html',
    'https://www.tennis-warehouse.com/Head_Speed_MP/descpageRCHEAD-HSPDM.html',
    'https://www.tennis-warehouse.com/Head_Speed_MP_Legend/descpageRCHEAD-HSPMPL.html',
    'https://www.tennis-warehouse.com/Head_Speed_Pro/descpageRCHEAD-HSPDP.html',
    'https://www.tennis-warehouse.com/Head_Speed_Pro_Legend/descpageRCHEAD-HSPDPL.html',
    'https://www.tennis-warehouse.com/Head_Boom_MP_Mint/descpageRCHEAD-BOOMMA.html',
    'https://www.tennis-warehouse.com/Head_Boom_MP/descpageRCHEAD-HBOOMM.html',
    'https://www.tennis-warehouse.com/Head_Titanium_TiS6_Strung/descpageRCHEAD-TIS6.html',
    'https://www.tennis-warehouse.com/Wilson_Blade_98_16x19_v9/descpageRCWILSON-WB9816.html',
    'https://www.tennis-warehouse.com/Wilson_Clash_100_Pro_v2/descpageRCWILSON-WC100P.html',
    'https://www.tennis-warehouse.com/Wilson_Clash_98_v2/descpageRCWILSON-WC98P.html',
    'https://www.tennis-warehouse.com/Wilson_Clash_100L_v2/descpageRCWILSON-WC10LV.html',
    'https://www.tennis-warehouse.com/Wilson_RF_01_Pro/descpageRCWILSON-WRFPR.html',
    'https://www.tennis-warehouse.com/Prince_Textreme_Warrior_100/descpageRCTWABG-W100.html',
    'https://www.tennis-warehouse.com/Prince_Classic_Graphite_107/descpageRCTWABG-CG107.html',
    'https://www.tennis-warehouse.com/Prince_ATS_Textreme_Tour_98/descpageRCTWABG-ATR98.html',
    'https://www.tennis-warehouse.com/Prince_Phantom_100P/descpageRCPRINCE-PHNP1.html',
    'https://www.tennis-warehouse.com/Yonex_EZONE_100_2025/descpageRCYONEX-EZ10BB.html',
    'https://www.tennis-warehouse.com/Yonex_EZONE_98_2025/descpageRCYONEX-EZ98BB.html',
    'https://www.tennis-warehouse.com/Yonex_Percept_100/descpageRCYONEX-PERC.html',
    'https://www.tennis-warehouse.com/Yonex_Percept_97/descpageRCYONEX-PERC97.html',
    'https://www.tennis-warehouse.com/Yonex_VCORE_100/descpageRCYONEX-VCR100.html',
    'https://www.tennis-warehouse.com/Yonex_VCORE_98_Tour/descpageRCYONEX-YVC98T.html',
    'https://www.tennis-warehouse.com/Yonex_VCORE_98/descpageRCYONEX-YVC98.html',
    'https://www.tennis-warehouse.com/Yonex_VCORE_100_Sand_Beige/descpageRCYONEX-VC10SB.html',
    'https://www.tennis-warehouse.com/Yonex_VCORE_98_Sand_Beige/descpageRCYONEX-VC98SB.html',
]

# Scraping function
def scrape_racquet(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return ["Error fetching page"] * 18

    soup = BeautifulSoup(response.text, 'html.parser')

    # Racquet name
    name_element = soup.find('h1', class_='desc_top-head-title')
    name = name_element.text.strip() if name_element else "Not found"

    # Price
    price_element = soup.find('span', class_='afterpay-full_price')
    price = price_element.text.strip() if price_element else "Not found"

    # Description
    description_element = soup.find('div', class_='check_read-inner', itemprop='description')
    if description_element:
        unwanted = description_element.find('i')
        if unwanted:
            unwanted.decompose()
        description = description_element.get_text(separator=' ', strip=True)
    else:
        description = "Not found"

    # Specs
    specs = soup.find_all('td', class_=['SpecsLt', 'SpecsDk'])
    spec_data = {
        'Head Size': None,
        'Length': None,
        'Strung Weight': None,
        'Balance': None,
        'Swingweight': None,
        'Stiffness': None,
        'Beam Width': None,
        'Composition': None,
        'Power Level': None,
        'Stroke Style': None,
        'Swing Speed': None,
        'Racquet Colors': None,
        'Grip Type': None,
        'String Pattern': None,
        'String Tension': None, 
    } 

    for spec in specs:
        text = spec.get_text(separator=' ', strip=True)
        for key in spec_data.keys():
            if key + ':' in text:
                spec_data[key] = text.replace(f'{key}:', '').strip()

    # Return all the data as a list
    return [
        name, price, description,
        spec_data['Head Size'], spec_data['Length'], spec_data['Strung Weight'],
        spec_data['Balance'], spec_data['Swingweight'], spec_data['Stiffness'],
        spec_data['Beam Width'], spec_data['Composition'], spec_data['Power Level'],
        spec_data['Stroke Style'], spec_data['Swing Speed'], spec_data['Racquet Colors'],
        spec_data['Grip Type'], spec_data['String Pattern'], spec_data['String Tension'],
    ]

# CSV file path
csv_file = 'racquets.csv'

# Write header only if file doesn't exist yet
file_exists = os.path.isfile(csv_file) 
 
# append data to csv 
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)

    # Write header only once
    if not file_exists:
        writer.writerow(['Name', 'Price', 'Description', 'Head Size', 'Length', 'Strung Weight', 'Balance', 'Swingweight', 'Stiffness', 'Beam Width', 'Composition', 'Power Level', 'Stroke Style', 'Swing Speed', 'Racquet Colors', 'Grip Type', 'String Pattern', 'String Tension'])

    # Loop through each URL and scrape data
    for url in urls:
        racquet_data = scrape_racquet(url)
        writer.writerow(racquet_data)
        print(f"Scraped: {racquet_data[0]}")
 