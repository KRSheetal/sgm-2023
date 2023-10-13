from geopy.geocoders import Nominatim
import requests
from statistics import mean

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
    
    result_time = data['daily']['time']
    result_temp = data['daily']['temperature_2m_mean']

    #print(result_time.index('2022-03-31'))
    # Q1_dates = result_time[0:90]
    Q1_temp = result_temp[0:90]
    Q1_mean = round(mean(Q1_temp))
 
    Q1_time_location = result_time.index
    # Q2_dates = result_time[91:180]
    Q2_temp = result_temp[91:180]
    Q2_mean = round(mean(Q2_temp))
    # print(result_time.index('2022-09-30'))
    # Q3_dates = result_time[180:272]
    Q3_temp = result_temp[181:272]
    Q3_mean = round(mean(Q3_temp))
    # print(result_time.index('2022-12-31'))
    # Q4_dates = result_time[272:364]
    Q4_temp = result_temp[273:364]
    Q4_mean = round(mean(Q4_temp))

    
    # dict = {}
        
    # for time_data, temp_data in zip(result_time, result_temp):
    #     dict[time_data] = temp_data
    
    # for time in dict.keys():
    #     if time == '2022-03-30':
    #         Q1 = dict[time]
    
    #     if time == '2022-06-30':
    #         Q2 = dict[time]
    
    #     if time == '2022-09-30':
    #         Q3 = dict[time]
  
    #     if time == '2022-12-30':
    #         Q4 = dict[time]

     
    quarterly_temp = {'Spring':Q1_mean, 'Summer': Q2_mean, 'Fall': Q3_mean, 'Winter': Q4_mean}
    print(quarterly_temp)

    #TODO write code to extract temperature_2m_mean quarterly and return to location_info.py

    return quarterly_temp # replace with temperature info
    

def get_coordinates(location):
    # get latitude and longitude for the city and state entered
    place = f'{location[0]} {location[1]}' # concatinate city and state to make one string
    geolocator = Nominatim(user_agent="city_co-ordinates")
    location = geolocator.geocode(place.replace(",", ""))
    longitude = location.longitude
    latitude = location.latitude
            
    return latitude, longitude


# added this for debugging purpose
location = ('minneapolis', 'minnesota')

climate_extracted_data = get_climate(location)
#print (f'Data from climate.py {climate_extracted_data}') 





