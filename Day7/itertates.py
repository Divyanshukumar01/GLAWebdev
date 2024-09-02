# Task-1
# Define a dictionary with countries and their states
countries_and_states = {
    'United States': ['California', 'New York', 'Texas'],
    'India': ['Maharashtra', 'Karnataka', 'Tamil Nadu'],
    'Australia': ['New South Wales', 'Victoria', 'Queensland']
}

# Iterate through countries and their states
for country, states in countries_and_states.items():
    print(f"States in {country}:")
    for state in states:
        print(f"  - {state}")


# Task-2: Iterate the lists and list the states with state properties- id,name,state_code, latitude, longitude, type.
state=[
{
    "id": 1,
    "name": "UttarPradesh",
    "state_code": 21,
    "latitude":36.7,
    "longitude":-54.9,
    "type":'State'
},
{
    "id": 2,
    "name": "HimachalPradesh",
    "state_code": 27,
    "latitude":76.8,
    "longitude":-89.9,
    "type":'State'
},
]

for state_info in state:
    id = state_info['id']
    name = state_info['name']
    state_code = state_info['state_code']
    latitude = state_info['latitude']
    longitude = state_info['longitude']
    type = state_info['type']

    print(f"State ID: {id}")
    print(f"State Name: {name}")
    print(f"State Code: {state_code}")
    print(f"Latitude: {latitude:.4f}")
    print(f"Longitude: {longitude:.4f}")
    print(f"Type: {type}")


# Task3: Read the resume.json file
import json

with open(r"C:\Users\Ishu Sambariya\Desktop\College\GLAWebdev\Day7\resume.json") as file:
    resume = json.load(file)
    for key, value in resume.items():
        print(key, value)


# Task4: Create a fxn and move this code inside the function & call for 5 times using loop
import json

def read_resume():
    with open(r"C:\Users\Ishu Sambariya\Desktop\College\GLAWebdev\Day7\resume.json") as file:
        resume = json.load(file)
        for key, value in resume.items():
            print(key, value)

for _ in range(5):
    read_resume()

# Task5: 
import json
# with open(r"C:\Users\Ishu Sambariya\Desktop\College\GLAWebdev\Day7\country.json",encoding="utf-8") as user_file:
#     data = json.load(user_file)
data = open(r"C:\Users\Ishu Sambariya\Desktop\College\GLAWebdev\Day7\country.json")
for country in data:
  print(f'country name {country["name"]}')
  for index ,state in enumerate(country["states"],1):
     print(f'{index}-> id :{state["id"]},  name:{state["name"]} , state_code :{state["state_code"]} , latitude:{state["latitude"]} , longitude: {state["longitude"] }')









