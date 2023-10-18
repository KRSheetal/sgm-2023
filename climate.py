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

    for month in time_temp_dictionary:
        month_number = month[5:7]

        january = '01'
        january_temps = []
        if month_number == january:
            january_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
            for jan_temp in january_dict.values():
                january_temps.append(jan_temp)
            january_average = sum(january_temps) / len(january_temps)

        april = '04'
        april_temps = []
        if month_number == april:
            april_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
            for apr_temp in april_dict.values():
                april_temps.append(apr_temp)
            april_average = sum(april_temps) / len(april_temps)

        august = '08'
        august_temps = []
        if month_number == august:
            august_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
            for aug_temp in august_dict.values():
                august_temps.append(aug_temp)
            august_average = sum(august_temps) / len(august_temps)

        november = '11'
        november_temps = []
        if month_number == november:
            november_dict = {k: v for k, v in time_temp_dictionary.items() if month_number in k[5:7]}
            for nov_temp in november_dict.values():
                november_temps.append(nov_temp)
            november_average = sum(november_temps) / len(november_temps)

        # if time == '2022-06-30':
        #     Q2 = time_temp_dictionary[time]
        #
        # if time == '2022-09-30':
        #     Q3 = time_temp_dictionary[time]
        #
        # if time == '2022-12-30':
        #     Q4 = time_temp_dictionary[time]

    quarterly_temp = {'January': january_average, 'April': april_average, 'August': august_average, 'November': november_average}
    # quarterly_temp = {'August': august_average, 'November': november_average}

    # TODO write code to extract temperature_2m_mean quarterly and return to location_info.py

    return quarterly_temp  # replace with temperature info


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
print(get_climate(location))

# climate_extracted_data = get_climate(location)
# print (f'Data from climate.py {climate_extracted_data}')