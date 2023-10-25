def display_menu_get_choice(menu):
    """ Displays all the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        message(menu)
        choice = input('Enter choice? ').upper()
        if menu.is_valid(choice):
            return choice
        else:
            message('Not a valid choice, please enter number or Q to quit.')


def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def bookmark_info():
    """ Ask user if they want the location information to be bookmarked """

    while True:
        bookmark_answer = input('Do you want to bookmark? (yes/no): ').upper()
        if bookmark_answer == 'YES':
            break
        elif bookmark_answer == 'NO':
            break
        else:
            message('Please enter Yes or No: ')


def show_bookmarked_list(data):
    """ Display bookmarked list or 'No bookmark message' """
    index = 0
    if data:
        for row in data:
            message(index, row)
            index += 1
    else:
        message('No bookmarks to display')


def get_location():
    """ Ask user for city and its state then returns city & state in title case"""

    city = input('Enter city: ')
    state = input('Enter the state: ')
    return city.title(), state.title()


def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)
