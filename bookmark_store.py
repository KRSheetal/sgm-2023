
# store location info on db

# columns = PRimary_key(city, state), cost_of_living, q1 temp, q2 temp, q3 temp, q4 temp, longitude, latitude
# save in bookmark.db
import sqlite3
import os 
import json
from datetime import datetime
import ui

db = os.path.join('database', 'bookmark_list.db')

# city = 'colorado springs'
# state = 'colorado'
# location = (city, state)

# data = {'Temperature': {'January': 56.32, 'April': 76.33, 'August': 64.33, 'November': 32.78}, 'Population': 6783, 'Cost_of_Living': 63732}

# Create bookmark table with required columns
def create_bookmark_table():
    bookmark_list = 'CREATE TABLE IF NOT EXISTS bookmark_list (city TEXT, state TEXT, cost_of_living INTEGER, population INTEGER, temperature STRING, date TEXT, UNIQUE( city COLLATE NOCASE, state COLLATE NOCASE))'
    con = sqlite3.connect(db)
    with con:
        con.execute(bookmark_list)
        con.close()


def bookmark_location_info(location, data):
   
    Temp_dict = data.get('Temperature')
    temp_dict_column = json.dumps(Temp_dict) # convert to string
    
    create_bookmark_table()
    # save the location information in bookmark table if does not exist
    insert_sql = 'INSERT OR IGNORE INTO bookmark_list (city, state, cost_of_living, population, temperature, date) VALUES (?, ?, ?, ?, ?,? )'
    try:
        with sqlite3.connect(db) as con:
            res = con.execute(insert_sql, (location[0], location[1], data.get('Cost_of_Living'),data.get('Population'), temp_dict_column, datetime.now()))
    except sqlite3.IntegrityError as e:
            raise BookMarkError(f'Error - this bookmark is already in the database. {data}') from e
    finally:
            con.close()


def get_all_bookmarked_list():
#             """ :returns entire bookmark list """
    conn = sqlite3.connect(db) # connect to sqlite
    cursor = conn.cursor() # create cursor object

    print('Location Information')

    data = cursor.execute('''Select * FROM bookmark_list''')

    ui.show_bookmarked_list(data)
    
    conn.commit()
    conn.close()

   
 # Source: https://www.geeksforgeeks.org/how-to-show-all-columns-in-the-sqlite-database-using-python/



class BookMarkError(Exception):
    """ For BookMarkStore errors. """
    pass


# bookmark_location_info(location, data)
# get_all_bookmarked_list()

