import requests

population_url = 'https://api.census.gov/data/2021/pep/population?get=POP_2021,NAME&for=STATE'
# response = requests.get(population_url)
# data = response.json()
# def get_population(city, state):
#     pass
# state = 'Nebraska'
# for inner_list in data:
#     # print(inner_list[0], inner_list[1])
#     state_population = inner_list[0]
#     # print(pop)
#     if inner_list[1] == state:
#         print(state)
#         print(state_population)
state = 'Minnesota'



def get_population(state):
    # extract state's population from the API
    response = requests.get(population_url)
    data = response.json()
    state_population = 0 # intialise

    # find the state and save its population from the list to the state_population variable
    for inner_list in data:
        #print(inner_list[0], inner_list[1])
        state_population = inner_list[0]
        if inner_list[1] == state:
            state_population = inner_list[0]

    return state_population


state_pop = get_population(state)
