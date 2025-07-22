# add_dummy_properties.py

import psycopg2
import uuid
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'realestate_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'Password'),
    'port': os.getenv('DB_PORT', '5432')
}

# -- Custom ID generator (same as in admin_routes.py) --
def generate_custom_property_id(conn):
    now = datetime.now()
    prefix = now.strftime("%Y-%m")          # e.g. "2025-07"
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM properties WHERE id LIKE %s",
        (f"{prefix}-%",)
    )
    count = cur.fetchone()[0] + 1           # next sequential number
    cur.close()
    return f"{prefix}-{count:03d}"          # e.g. "2025-07-001"

# -- Dummy data for Kolkata City properties (20 total) --
dummy_properties = [
    {'title': '3BHK Modern Apartment in Salt Lake',      'price': 5500000.00,  'location': 'Salt Lake, Kolkata',     'bedrooms': 3, 'bathrooms': 2, 'area': 1200.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Luxury Villa in New Town',                'price':12500000.00,  'location': 'New Town, Kolkata',        'bedrooms': 5, 'bathrooms': 4, 'area': 3500.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Cozy 1BHK Studio in Ballygunge',           'price': 3000000.00,  'location': 'Ballygunge, Kolkata',      'bedrooms': 1, 'bathrooms': 1, 'area': 500.00,  'source': 'Dummy', 'status': 'Inactive', 'image': None},
    {'title': 'Spacious 2BHK Flat near Park Street',      'price': 7800000.00,  'location': 'Park Street, Kolkata',      'bedrooms': 2, 'bathrooms': 2, 'area': 1400.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Affordable 3BHK in Behala',               'price': 4200000.00,  'location': 'Behala, Kolkata',          'bedrooms': 3, 'bathrooms': 2, 'area': 1100.00, 'source': 'Dummy', 'status': 'Inactive', 'image': None},
    {'title': '4BHK Duplex in Jadavpur',                 'price': 8500000.00,  'location': 'Jadavpur, Kolkata',        'bedrooms': 4, 'bathrooms': 3, 'area': 2200.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Penthouse in Elgin Road',                 'price': 15000000.00, 'location': 'Elgin Road, Kolkata',      'bedrooms': 3, 'bathrooms': 3, 'area': 1800.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Studio Apartment in Howrah',              'price': 2600000.00,  'location': 'Howrah, Kolkata',          'bedrooms': 1, 'bathrooms': 1, 'area': 550.00,  'source': 'Dummy', 'status': 'Inactive', 'image': None},
    {'title': '5BHK Mansion in Alipore',                 'price': 22500000.00, 'location': 'Alipore, Kolkata',         'bedrooms': 5, 'bathrooms': 5, 'area': 5000.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': '2BHK Apartment in Dum Dum',               'price': 3800000.00,  'location': 'Dum Dum, Kolkata',          'bedrooms': 2, 'bathrooms': 2, 'area': 900.00,  'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': '3BHK Row House in Garia',                 'price': 6300000.00,  'location': 'Garia, Kolkata',           'bedrooms': 3, 'bathrooms': 2, 'area': 1300.00, 'source': 'Dummy', 'status': 'Inactive', 'image': None},
    {'title': '1BHK Affordable Flat in Howrah Maidan',   'price': 2100000.00,  'location': 'Howrah Maidan, Kolkata',  'bedrooms': 1, 'bathrooms': 1, 'area': 450.00,  'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': '4BHK Corner Flat in Salt Lake Sector V',   'price': 9800000.00,  'location': 'Salt Lake Sector V, Kolkata','bedrooms': 4,'bathrooms': 3,'area': 2000.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Luxury Studio near Victoria Memorial',    'price': 5200000.00,  'location': 'Esplanade, Kolkata',       'bedrooms': 1, 'bathrooms': 1, 'area': 650.00,  'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': '5BHK Independent House in Tollygunge',     'price': 14000000.00, 'location': 'Tollygunge, Kolkata',      'bedrooms': 5, 'bathrooms': 4, 'area': 4000.00, 'source': 'Dummy', 'status': 'Inactive', 'image': None},
    {'title': 'Eco-Friendly Villa in Rajarhat',          'price': 11000000.00, 'location': 'Rajarhat, Kolkata',        'bedrooms': 4, 'bathrooms': 3, 'area': 3000.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Compact Flat in Sealdah',                 'price': 2900000.00,  'location': 'Sealdah, Kolkata',         'bedrooms': 2, 'bathrooms': 1, 'area': 700.00,  'source': 'Dummy', 'status': 'Inactive', 'image': None},
    {'title': '3BHK Penthouse in Barrackpore',           'price': 9200000.00,  'location': 'Barrackpore, Kolkata',     'bedrooms': 3, 'bathrooms': 2, 'area': 1600.00, 'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': '2BHK Flat in Howrah Santoshpur',          'price': 4500000.00,  'location': 'Santoshpur, Kolkata',      'bedrooms': 2, 'bathrooms': 2, 'area': 950.00,  'source': 'Dummy', 'status': 'Active',   'image': None},
    {'title': 'Spacious Villa in Bally, Howrah',         'price': 13000000.00, 'location': 'Bally, Howrah',           'bedrooms': 5, 'bathrooms': 4, 'area': 4200.00, 'source': 'Dummy', 'status': 'Inactive', 'image': None},
]

def insert_dummy_properties():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for prop in dummy_properties:
            # 1. Generate the monthly custom ID
            prop_id = generate_custom_property_id(conn)

            # 2. Insert using the same columns/order as your POST route
            cursor.execute("""
                INSERT INTO properties
                  (id, title, price, location,
                   bedrooms, bathrooms, area,
                   source, status, image, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """, (
                prop_id,
                prop['title'].strip(),
                prop['price'],
                prop['location'].strip(),
                prop['bedrooms'],
                prop['bathrooms'],
                prop['area'],
                prop['source'].strip(),
                prop['status'].strip(),
                prop['image']
            ))

            print(f"Inserted [{prop_id}]: {prop['title']}")

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ All dummy properties inserted successfully.")

    except Exception as e:
        print(f"Error inserting dummy properties: {e}")

if __name__ == '__main__':
    insert_dummy_properties()
