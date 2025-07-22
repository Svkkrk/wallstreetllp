# update_property_images.py

import os
import random
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# --- your DB connection settings (same as before) ---
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'realestate_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'Password'),
    'port': os.getenv('DB_PORT', '5432')
}

# --- folder where your images live ---
UPLOAD_FOLDER = 'static/uploads'

def assign_images_to_properties():
    # 1. Grab all image filenames
    images = [
        fname for fname in os.listdir(UPLOAD_FOLDER)
        if fname.lower().startswith('property') and fname.lower().endswith('.jpg')
    ]
    if not images:
        print("❌ No property*.jpg files found in", UPLOAD_FOLDER)
        return

    random.shuffle(images)

    # 2. Connect to DB and fetch all property IDs
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id FROM properties ORDER BY updated_at")
    prop_ids = [row[0] for row in cur.fetchall()]

    if not prop_ids:
        print("❌ No properties found in the database.")
        cur.close()
        conn.close()
        return

    # 3. Assign images in a round‑robin fashion
    for idx, prop_id in enumerate(prop_ids):
        image_fname = images[idx % len(images)]
        cur.execute(
            "UPDATE properties SET image = %s, updated_at = NOW() WHERE id = %s",
            (image_fname, prop_id)
        )
        print(f"→ Property {prop_id} ← image set to {image_fname}")

    # 4. Commit and cleanup
    conn.commit()
    cur.close()
    conn.close()
    print("✅ All properties updated with random images.")

if __name__ == '__main__':
    assign_images_to_properties()
