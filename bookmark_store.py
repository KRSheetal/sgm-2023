
# store location info on db

# columns = PRimary_key(city, state), cost_of_living, q1 temp, q2 temp, q3 temp, q4 temp, longitude, latitude
# save in bookmark.db
import sqlite3
import os 
import json

db = os.path.join('database', 'bookmark_list.db')

city = 'denver'
state = 'colorado'
location = (city, state)

data = {'Temperature': {'January': 56.32, 'April': 76.33, 'August': 64.33, 'November': 32.78}, 'Population': 6783, 'Cost_of_Living': 63732}



def bookmark_location_info(location, data):
   
    Temp_dict = data.get('Temperature')
    temp_dict_column = json.dumps(Temp_dict)

    print(data)
    print(Temp_dict)
    print(temp_dict_column)
    print(Temp_dict.get('January'))

    January_2022 = 0

    for month, temp in Temp_dict.items():
         if month == 'January':
              January_2022 = temp

    print(January_2022)
    
    


    
    
    create_bookmark_table()
    
    insert_sql = 'INSERT INTO bookmark_list (city, state, cost_of_living, population, temperature) VALUES (?, ?, ?, ?, ? )'
    try:
        with sqlite3.connect(db) as con:
            res = con.execute(insert_sql, (location[0], location[1], data.get('Cost_of_Living'),temp_dict_column, data.get('Temperature')))
            new_id = res.lastrowid  # Get the ID of the new row in the table
            location.id = new_id  # Set this book's ID
    except sqlite3.IntegrityError as e:
            raise BookMarkError(f'Error - this bookmark is already in the database. {data}') from e
    finally:
            con.close()


def create_bookmark_table():
    bookmark_list = 'CREATE TABLE IF NOT EXISTS bookmark_list (city TEXT, state TEXT, cost_of_living INTEGER, population INTEGER, temperature ENT, UNIQUE( city COLLATE NOCASE, state COLLATE NOCASE))'
    con = sqlite3.connect(db)
        
    with con:
        con.execute(bookmark_list)
        con.close()


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


bookmark_location_info(location, data)

