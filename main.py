""" Program to assist user in making a moving decision based on cost of living, climate, and population"""

from menu import Menu
import ui
import location_info
import bookmark_store


def main():
    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Find location information', find_location_info)
    menu.add_option('2', 'View Bookmarked list', view_bookmarked_list)
    menu.add_option('Q', 'Quit', quit_program)
    return menu


def find_location_info():
    """ Ask user to enter city and state name then
    display population, climate & cost-of-living info of entered location """

    location = ui.get_location()
    location_data = location_info.get_location_info(location)
    ui.message(f'View information of {location[0]} {location[1]} to make a decision')
    for category, data in location_data.items():
        if category == 'Temperature':
            ui.message(f'The quarterly temperature(F) of {location[0]} in the year 2022 is \n {data}:')
        elif category == 'Population':
            ui.message(f'The population of the {location[1]} is: {data}')
        else:
            ui.message(f'The {category} is: ${data}')
    bookmark_information = ui.bookmark_info()
    if bookmark_information:
        bookmark_store.bookmark_location_info(location, location_data)
        ui.message('Location information bookmarked!')
    else:
        ui.message('Location information NOT bookmarked!')
        return


def view_bookmarked_list():
    """ display locations with population, climate & cost-of-living info
    that are bookmarked list by the user """
    bookmarks = bookmark_store.get_all_bookmarked_list()
    ui.show_bookmarked_list(bookmarks)


def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
