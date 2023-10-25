from geopy.geocoders import Nominatim
import requests

climate_url_temp = 'https://climate-api.open-meteo.com/v1/climate?&start_date=2022-01-01&end_date=2022-12-31&models=FGOALS_f3_H&temperature_unit=fahrenheit&daily=temperature_2m_mean'

def get_climate(location):
    # get longitude and latitude for the city and state as this API requires longitude
    # and latitude to show the climate data
    latitude, longitude = get_coordinates(location)

    # prepare API url to get climate data
    data = extract_climate_data(latitude, longitude)
    result_time = get_date(data) 
    result_temp = get_temperature(data)

    time_temp_dictionary = create_date_temp_dict(result_time, result_temp)
    
    # Find temperature average of the months in all 4 seasons
    january = '01'
    january_average = get_monthwise_temperature(time_temp_dictionary, january)

    april = '04'
    april_average = get_monthwise_temperature(time_temp_dictionary, april)

    august = '08'
    august_average = get_monthwise_temperature(time_temp_dictionary, august)

    november = '11'
    november_average = get_monthwise_temperature(time_temp_dictionary, november)
    
    quarterly_temp = {'January': january_average, 'April': april_average, 'August': august_average, 'November': november_average}

    return quarterly_temp

def extract_climate_data(latitude, longitude):
    query = {'latitude': latitude, 'longitude': longitude}
    return api_url_response(query)
   
def api_url_response(query):
    res = requests.get(climate_url_temp, params=query).json()
    return res

def get_date(data):
    return data['daily']['time']

def get_temperature(data):
    return data['daily']['temperature_2m_mean']


def create_date_temp_dict(result_time, result_temp):
    time_temp_dictionary = {}
    for time_data, temp_data in zip(result_time, result_temp):
        time_temp_dictionary[time_data] = temp_data
    return time_temp_dictionary


def get_monthwise_temperature(time_temp_dictionary, month_num):
        month_number = 0
        for month in time_temp_dictionary:
            month_number = month[5:7] # extract month number from the date(key)
                
            month_temps = []
            
            if month_number == month_num: # if month_num found
                # create month: temperature dictionary
                month_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
                # create a list with temperatures
                for month_temp in month_dict.values():
                    month_temps.append(month_temp)

                month_average = round(sum(month_temps) / len(month_temps))

                return month_average

def get_coordinates(location):
    # get latitude and longitude for the city and state entered
    place = f'{location[0]} {location[1]}'  # concatinate city and state to make one string
    geolocator = Nominatim(user_agent="city_co-ordinates")
    location = geolocator.geocode(place.replace(",", ""))
    longitude = location.longitude
    latitude = location.latitude
    # print(longitude, latitude)

    return latitude, longitude



# climate_extracted_data = get_climate(location)
# print (f'Data from climate.py {climate_extracted_data}')