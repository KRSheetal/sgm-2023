import climate
from geopy.geocoders import Nominatim


'''Write action code as per main.py'''
# API manager

climate_url_temp = 'https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=2022-01-01&end_date=2022-12-31&models=FGOALS_f3_H&temperature_unit=fahrenheit&daily=temperature_2m_mean'
population_url_by_state = 'https://api.census.gov/data/2021/pep/population?get=POP_2021,NAME&for=STATE:*'

def main():

    def get_location_info(location):
    
    # Climate
        longitude_latitude = get_longitude_latitude(location)
        temp_mean_quarterly = climate.get_climate(longitude_latitude)
        
    # Population
    
    ######state = location(state)


        


    # Cost of living
    pass

    def get_longitude_latitude():
        #get Longitute and latitude for the city and state entered
        '''
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode("175 5th Avenue NYC")

    print(location.address)
    # Output: Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...

    print((location.latitude, location.longitude))
    # Output: (40.7410861, -73.9896297241625)

    print(location.raw)
    # Output: {'place_id': '9167009604', 'type': 'attraction', ...}
        '''
    pass

    

    # call pop API func
    # Call COL func
    # CAll Climate func

#climate.get_climate(city, state)
    # assmeble data, return
   

""" class Climate

#city
state
temps - How will this be saved (SQLite)"""




if __name__ == '__main__':
    main()


