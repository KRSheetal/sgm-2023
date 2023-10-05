""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from menu import Menu
import ui

#store = LocationInfo()

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        print(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Find location information', find_location_info)
    menu.add_option('2', 'Update Bookmarked status', change_bookmark)
    menu.add_option('3', 'View Bookmarked list', view_bookmarked_list) 
    menu.add_option('Q', 'Quit', quit_program)

    return menu

def find_location_info():

    new_location = ui.get_location()

   # location_info = store.get_location_info()

    ui.message(f'View information of {new_location} to make a decision')
    # ui.message(location_info)

    return
#     '''TODO: Ask user to enter city and its 2 letter state code and
#       display population, climate & cost-of-living info of entered location'''
    
#     # first look in the info in the cache.db, 
#     # if cache.db has the location info
#     #       if the info is 1 hour old make a new API call & replace the location & result in cache.db
#     #       else if it not old, display the location info
#     # else if the location not found in the cache.db, make new API call and save the result in cache.db


#     # TODO: Ask if user wants to bookmark the result. If yes, add to bookmark.db with time of the result displayed
    

def view_bookmarked_list():
#     '''TODO: write code to display locations with population, climate & cost-of-living info
#       that are bookmarked list by user'''
#     bookmarks = store.get_all_bookmarked_list()
#     ui.show_bookmarked_list(bookmarks)
    return
    

def change_bookmark():
#     ''' TODO: Display the bookmark list and ask user to unbookmark the location info
#     from the bookmarked list & update the bookmark list'''
#     bookmark_id = ui.get_bookmarked_id()
#     bookmark = store.get_bookmarked_item_by_id(bookmark_id)
#     # TODO: Unbookmark the location
    return


def quit_program():
    ui.message('Thanks and bye!')

if __name__ == '__main__':
    main()
