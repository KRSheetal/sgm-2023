# grant
from unittest import TestCase
from unittest.mock import patch
import os

import bookmark_store
# from bookmark_store import Bookmark, BookmarkStore

import ui
from menu import Menu


class TestUI(TestCase):

    @classmethod
    def setUpClass(cls):
        bookmark_store.db = os.path.join('database', 'test_bookmark_list.db')
        # BookStore.instance = None

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_display_menu_get_choice(self, mock_print, mock_input):
        menu = Menu()
        menu.add_option('1', '123', lambda: None)
        menu.add_option('2', '456', lambda: None)

        self.assertEqual('1', ui.display_menu_get_choice(menu))

        mock_print.assert_any_call(menu)

    @patch('builtins.print')
    def test_message(self, mock_print):
        ui.message('hello')
        mock_print.assert_called_with('hello')

    @patch('builtins.print')
    def test_show_bookmarks_empty(self, mock_print):
        bookmarks = []
        ui.show_bookmarked_list(bookmarks)
        mock_print.assert_called_with('No bookmarks to display')

    # @patch('builtins.print')
    # def test_show_bookmarks_list(self, mock_print):
    #     location1 = Bookmark('a', 'aaa')
    #     location2 = Bookmark('b', 'bbb')
    #     bookmarks = [location1, location2]
    #     ui.show_bookmarked_list(bookmarks)
    #
    #     mock_print.assert_any_call(location1)
    #     mock_print.assert_any_call(location2)

    @patch('builtins.input', side_effect=['city', 'state'])
    def test_get_location(self, mock_input):
        location = ui.get_location()
        self.assertEqual('city', location[0])
        self.assertEqual('state', location[1])

    @patch('builtins.input', side_effect=['pizza'])
    @patch('builtins.print')
    def ask_question(self, mock_print, mock_input):
        self.assertEqual('pizza', ui.ask_question('What is your favorite food?'))
        mock_print.assert_called_with('What is your favorite food?')
