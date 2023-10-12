from geopy.geocoders import Nominatim
import requests

# climate data
climate_url_temp = 'https://climate-api.open-meteo.com/v1/climate?&start_date=2022-01-01&end_date=2022-12-31&models=FGOALS_f3_H&temperature_unit=fahrenheit&daily=temperature_2m_mean'
    
def get_climate(location):
    # get longitude and latitude for the city and state as this API requires longitude 
    # and latitude to show the climate data
    latitude,longitude = get_coordinates(location)
        
    # prepare API url to get climate data
    query = {'latitude':latitude,'longitude':longitude}
    response = requests.get(climate_url_temp, params=query)
    data = response.json()

    #TODO write code to extract temperature_2m_mean quarterly and return to location_info.py

    return data # replace with temperature info
    

def get_coordinates(location):
    # get latitude and longitude for the city and state entered
    place = f'{location[0]} {location[1]}' # concatinate city and state to make one string
    geolocator = Nominatim(user_agent="city_co-ordinates")
    location = geolocator.geocode(place.replace(",", ""))
    longitude = location.longitude
    latitude = location.latitude
            
    return latitude, longitude

# added this for debugging purpose
# location = ('minneapolis', 'minnesota')

# climate_extracted_data = get_climate(location)
# print (f'Data from climate.py {climate_extracted_data}') 





