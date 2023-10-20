from geopy.geocoders import Nominatim
import requests

# climate data
climate_url_temp = 'https://climate-api.open-meteo.com/v1/climate?&start_date=2022-01-01&end_date=2022-12-31&models=FGOALS_f3_H&temperature_unit=fahrenheit&daily=temperature_2m_mean'


def get_climate(location):
    # get longitude and latitude for the city and state as this API requires longitude
    # and latitude to show the climate data
    latitude, longitude = get_coordinates(location)

    # prepare API url to get climate data
    query = {'latitude': latitude, 'longitude': longitude}
    response = requests.get(climate_url_temp, params=query)
    data = response.json()

    result_time = data['daily']['time']
    result_temp = data['daily']['temperature_2m_mean']

    time_temp_dictionary = {}

    for time_data, temp_data in zip(result_time, result_temp):
        time_temp_dictionary[time_data] = temp_data
    # print(time_temp_dictionary)

    # extract month number from the date
    # for month in time_temp_dictionary:
    #     month_number = month[5:7]
    #     print(month_number)

        # january = '01'
        # january_temps = []
        # if month_number == january:
        #     january_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
        #     for jan_temp in january_dict.values():
        #         january_temps.append(jan_temp)
        #     january_average = sum(january_temps) / len(january_temps)
    
    # print(month_number)
   

        january = '01'
        january_average = get_monthwise_temperature(time_temp_dictionary, january)

        april = '04'
        april_average = get_monthwise_temperature(time_temp_dictionary, april)

        # august = '08'
        # august_average = get_monthwise_temperature(time_temp_dictionary, august)

        # november = '11'
        # november_average = get_monthwise_temperature(time_temp_dictionary, november)

       # quarterly_temp = {'January': round(january_average), 'April': round(april_average), 'August': round(august_average), 'November': round(november_average)}
        print(january_average)
        print(april_average)
        return #quarterly_temp  # replace with temperature info

def get_monthwise_temperature(time_temp_dictionary, month_num):
        month_number = ''
        print(month_num, month_number)
        for date, temp in time_temp_dictionary.items():
            month_number = date[5:7]
                
            month_temps = []
            print(month_num, month_number)
            if month_number == month_num:
                month_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
                for month_temp in month_dict.values():
                    month_temps.append(month_temp)
                month_average = sum(month_temps) / len(month_temps)
        
                return month_average
        print(month_number)


def get_coordinates(location):
    # get latitude and longitude for the city and state entered
    place = f'{location[0]} {location[1]}'  # concatinate city and state to make one string
    geolocator = Nominatim(user_agent="city_co-ordinates")
    location = geolocator.geocode(place.replace(",", ""))
    longitude = location.longitude
    latitude = location.latitude

    return latitude, longitude

# # added this for debugging purpose
location = ('Minneapolis', 'Minnesota')


climate_extracted_data = get_climate(location)
print (f'Data from climate.py {climate_extracted_data}')