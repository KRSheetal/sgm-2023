from location_info import location


def display_menu_get_choice(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('Enter choice? ').upper()  # .upper() converts the input string to upper case to remove case sensitivity.
                                                  # Quit, and any future options that use a letter input, can now be done
                                                  # with a lower case or upper case input.
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')


def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def show_bookmarked_list(books):
    '''Display bookmarked list or 'No bookmark message'''
    # TODO : show bookmarked list. If empty, display 'No bookmark' message

def get_bookmarked_id():
    """ Ask for ID, validate to ensure is positive integer
    :returns: the ID value """
    while True:
        try:
            id = int(input('Enter book ID: '))
            if id > 0:
                return id
            else:
                print('Please enter a positive number.')

        except ValueError:
            print('Please enter a number.')
   


def get_location():
    """ Ask user for city and its country code to add to the url
     :returns: city & country code. """
    city = input('Enter city: ')
    country_code = input('Enter 2 letter country code: ')
    return Location(city, country_code)

def get_location_info():



def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)
