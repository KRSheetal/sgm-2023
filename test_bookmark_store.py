import sqlite3
import unittest
import os
from unittest import TestCase

import bookmark_store
from bookmark_store import BookMarkError

import ui
from ui import show_bookmarked_list

test_db_url = os.path.join('database', 'test_bookmark_store.db')


class TestBookmark_Store(TestCase):
    test_db_url = 'test_bookmark_store.db'
    test_bookmark_list = 'CREATE TABLE IF NOT EXISTS test_bookmark_list (city TEXT, state TEXT, cost_of_living INTEGER, population INTEGER, temperature STRING, date TEXT, UNIQUE( city COLLATE NOCASE, state COLLATE NOCASE))'
    conn = sqlite3.connect(test_db_url)
    with conn:
        conn.execute(test_bookmark_list)
        # conn.close()

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the bookstore db_url with the test database URL
        bookmark_store.db = self.test_db_url
        # drop everything from the DB to always start with an empty database
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DELETE FROM test_bookmark_list')
        conn.close()

    def test_bookmark_location_info(self):
        location1 = 'denver, colorado'
        data1 = {'Temperature': {'January': 56.32, 'April': 76.33, 'August': 64.33, 'November': 32.78}, 'Population': 6783, 'Cost_of_Living': 63732}
        bookmark_store.bookmark_location_info(location1, data1)
        expected = {location1, data1}
        self.compare_db_to_expected(expected)   
        
        location2 = 'tampa, florida'
        data2 = {'Temperature': {'January': 64, 'April': 71, 'August': 82, 'November': 66}, 'Population': 732673, 'Cost_of_Living': 8525}
        bookmark_store.bookmark_location_info(location2, data2)
        expected = {location2, data2}
        self.compare_db_to_expected(expected)


        # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):

        print(expected)

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM test_bookmark_list').fetchall()
        print(all_data)

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # city info exists, and data is correct
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])
            conn.close()


    if __name__ == '__main__':
        unittest.main()

    




