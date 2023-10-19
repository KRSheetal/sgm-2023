#from location_info import location




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

def bookmark_info():
    """Ask user if the Location information needs to be bookmarked"""
  
    while True:
        try:
            bookmark_answer = input("Do you want to bookmark? (yes/no): ")
            if bookmark_answer == 'YES':
                return True
            elif bookmark_answer == 'NO':
                return False
            else:
                bookmark_answer = input('Please type yes or no only: ')
        except ValueError:
            print('Please enter a alphabetical characters')
                

def show_bookmarked_list(data):
    '''Display bookmarked list or 'No bookmark message'''
    index = 0
    if data:
        for row in data:
            print(index, row)
            index += 1
    else:
        print('No bookmarks to display')


def get_location():
    """ Ask user for city and its country code to add to the url
     :returns: city & country code. """
    city = input('Enter city: ')
    
    state = input('Enter the state: ')
    return (city, state)



def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)
