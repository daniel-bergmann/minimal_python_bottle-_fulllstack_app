# sqlite is part of python
import sqlite3
import requests
import random
from faker import Faker

############################

fake = Faker()

#print(fake.city())
#exit()

############################

db = sqlite3.connect("./data/database.db")
q = """
DROP TABLE IF EXISTS items;
CREATE TABLE items(
    item_id         TEXT PRIMARY KEY,
    item_name       TEXT,
    item_price      INTEGER,
    item_picture_path   TEXT,
    item_city_name  TEXT,
    item_paragraph  TEXT
) WITHOUT ROWID
"""
# run multiple sql commands at once
db.executescript(q)
##################################
# Insert only 1 item
# user_id = str(fake.uuid4().replace("-",""))
# print(user_id)
# user_first_name = fake.first_name()
# print(user_first_name)
# price = random.randint(1000, 20000)
# print(price)
# # exit()
# q = f"INSERT INTO items VALUES ('{user_id}', '{user_first_name}', )
# db.execute(q)
# db.commit()
######################################

#######################################

# Get path to pictures and store the paths in a list
category = "furniture"
total_images = 500
response = requests.get(f"https://api.unsplash.com/search/photos?per_page={total_images}&query={category}&client_id=XXXXXXXXXXXXXXXXXXX")
response = response.json()
results = response["results"]
images = []
for result in results:
    urls = result["urls"]
    regular = urls["regular"]
    images.append(regular)


items = []
# Change the number in the () to select the amount of items in the DB
for _ in range(500):
    item_id = str(fake.uuid4().replace("-", ""))
    item_first_name = fake.first_name()
    item_price = random.randint(1000, 20000)
    random_index = random.randint(0, (len(images)-1))
    item_picture_path = images[random_index]
    item_city_name = fake.city()
    item_paragraph = fake.paragraph(nb_sentences=3)
    item = (item_id, item_first_name, item_price, item_picture_path, item_city_name, item_paragraph)
    items.append(item)
db.executemany("INSERT INTO items VALUES(?, ?, ?, ?, ?, ?)", items)
db.commit()
db.close()


# To create a virtual environment
# python -m venv .
# press "s" and then the TAB button .\Scripts\ should pop up
# press "a"  and then the TAB button for .\Scripts\activate\
# only type .\Scripts\activate\ to start the venv
# to install pip: python -m pip install  
# pip install requests
# pip install faker
# pip install bottle
# pip install paste

# requests is similar to node_modules