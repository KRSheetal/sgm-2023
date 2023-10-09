import climate
import population
import cost_of_living


def get_location_info(location):
   
    
    # Get climate data from climate.py
    temp_mean_quarterly = climate.get_climate(location)
    # print(temp_mean_quarterly)

    #city
    '''state
    temps - How will this be saved (SQLite)'''
         
    # Get population by state from population.py
    population_data = population.get_population(location[1])
    

    # Get Cost-of-living data from cost_of_living.py
    cost_of_living_data = cost_of_living.get_cost_of_living(location)
    

    # assmeble data on a dictionary, return
    location_info_dict = {'Temperature': temp_mean_quarterly, 'Population': population_data, 'Cost_of_Living': cost_of_living_data}
    return location_info_dict 


    
   






