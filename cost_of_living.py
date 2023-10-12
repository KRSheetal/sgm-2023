import os
import requests

import state_name_state_code_dictionary

key = os.environ.get('COST_OF_LIVING_KEY')

def get_cost_of_living(city, state):
    city_name = city
    state_name = state
    for state in state_name_state_code_dictionary.states_and_state_codes:
        state_code = state_name_state_code_dictionary.states_and_state_codes[state]
        if state == state_name:
            url = f'https://www.numbeo.com//api/city_cost_estimator?api_key={key}&query={city_name},%20{state_code},%20United%20States&members=1&children=0&include_rent=true&currency=USD'
            data = requests.get(url).json()
            cost_of_living = data.get('overall_estimate')
            return cost_of_living

# print(get_cost_of_living('Minneapolis', 'Minnesota'))