import requests

url = 'https://api.census.gov/data/2021/pep/population?get=POP_2021,NAME&for=STATE'
response = requests.get(url)
data = response.json()
def get_population(city, state_code):
    pass
state = 'Nebraska'
for inner_list in data:
    # print(inner_list[0], inner_list[1])
    state_population = inner_list[0]
    # print(pop)
    if inner_list[1] == state:
        print(state)
        print(state_population)