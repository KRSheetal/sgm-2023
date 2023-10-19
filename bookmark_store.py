
# store location info on db

# columns = PRimary_key(city, state), cost_of_living, q1 temp, q2 temp, q3 temp, q4 temp, longitude, latitude
# save in bookmark.db
import sqlite3
import os 
import json
from datetime import datetime

db = os.path.join('database', 'bookmark_list.db')

# city = 'denver'
# state = 'colorado'
# location = (city, state)

# data = {'Temperature': {'January': 56.32, 'April': 76.33, 'August': 64.33, 'November': 32.78}, 'Population': 6783, 'Cost_of_Living': 63732}



def bookmark_location_info(location, data):
   
    Temp_dict = data.get('Temperature')
    temp_dict_column = json.dumps(Temp_dict) # convert to string
    
    create_bookmark_table()
    # save the location information in bookmark table
    insert_sql = 'INSERT INTO bookmark_list (city, state, cost_of_living, population, temperature, date) VALUES (?, ?, ?, ?, ?,? )'
    try:
        with sqlite3.connect(db) as con:
            res = con.execute(insert_sql, (location[0], location[1], data.get('Cost_of_Living'),data.get('Population'), temp_dict_column, datetime.now()))
    except sqlite3.IntegrityError as e:
            raise BookMarkError(f'Error - this bookmark is already in the database. {data}') from e
    finally:
            con.close()

# Create bookmark table with required columns 
def create_bookmark_table():
    bookmark_list = 'CREATE TABLE IF NOT EXISTS bookmark_list (city TEXT, state TEXT, cost_of_living INTEGER, population INTEGER, temperature STRING, date TEXT, UNIQUE( city COLLATE NOCASE, state COLLATE NOCASE))'
    con = sqlite3.connect(db)
       
    with con:
        con.execute(bookmark_list)
        #con.close()


# def get_all_books(self):
#             """ :returns entire book list """
    
#             get_all_books_sql = 'SELECT rowid, * FROM books'

#             con = sqlite3.connect(db)
#             con.row_factory = sqlite3.Row
#             rows = con.execute(get_all_books_sql)
#             books = []

#             for r in rows:
#                 book = Book(r['title'], r['author'], r['read'], r['rowid'])
#                 books.append(book)

#             con.close()            
            
#             return books


class BookMarkError(Exception):
    """ For BookMarkStore errors. """
    pass


# bookmark_location_info(location, data)

