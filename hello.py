name = "goose"
greeting = f"Hello, {name}!"
print(greeting)

countries = ["UK", "France", "Ireland", "Japan", "Kenya"]
for country in  countries:
    print(f"I want to visit {country}")

def greet_traveller(destination):
    return f"Get ready - {destination} awaits!"

message = greet_traveller("Japan")
print(message)

message = greet_traveller("Kenya")
print(message)

country_info = {
    "name": "Kenya",
    "continent": "Africa",
    "population": 48000000,
    "capital": "Nairobi"
}


print(country_info["name"])
print(country_info["population"])
print(country_info["capital"])

population = country_info["population"]

if population > 50000000:
    print("That's a big population!")
else:
    print("That's a smaller population")
