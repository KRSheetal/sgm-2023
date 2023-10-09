import climate



'''Write action code as per main.py'''
# API manager


population_url_by_state = 'https://api.census.gov/data/2021/pep/population?get=POP_2021,NAME&for=STATE:*'

def get_location_info(location):
   
    # Climate
    temp_mean_quarterly = climate.get_climate(location)
    # print(temp_mean_quarterly)

    """ class Climate

#city
state
temps - How will this be saved (SQLite)"""
 
        
    # Population
    
    # ######state = location(state)


    # # Cost of living
    # pass

    # assmeble data, return
    return temp_mean_quarterly # replace with gathered data (climate, population & cost_of_living)


    
   






