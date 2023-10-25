import os
import requests

import state_name_state_code_dictionary

key = os.environ.get('COST_OF_LIVING_KEY')

state_code_dict = state_name_state_code_dictionary.states_and_state_codes

cost_of_living_url = f'https://www.numbeo.com//api/city_cost_estimator?%20United%20States&members=1&children=0&include_rent=true&currency=USD'

def get_cost_of_living(location):
    city_name = location[0]
    state_name = location[1]
    

    for state, state_code in state_code_dict.items():
        if state == state_name.title():
            # print(state_name.title())
            state_code = state_code_dict[state]
            cost_of_living_url = f'https://www.numbeo.com//api/city_cost_estimator?api_key={key}&query={city_name},%20{state_code},%20United%20States&members=1&children=0&include_rent=true&currency=USD'
            data = requests.get(cost_of_living_url).json()
            cost_of_living = data.get('overall_estimate')
            return round(cost_of_living)
        
# city = 'minneapolis'
# state = 'minnesota'
# location = city, state
# col = get_cost_of_living(location)
# print(col)