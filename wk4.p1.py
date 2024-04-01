rivers = {
    'Nile River':['Egypt', 'Sudan', 'Uganda', 'Ethopia', 'Kenya', 'Tanzania', 'Rwanda', 'Burundi', 'Democratric Republic of the Congo'], 
    'Amazon River':['Brazil', 'Peru', 'Colombia', 'Venezuela', 'Ecuador', 'Bolivia', 'Guyana'], 
    'Mississippi River': ['United States of America', 'Canada']
    }

#2: Statement about Each River and Countries it runs through
for river, countries in rivers.items():
    countries_str = ', '.join(countries)
    print(f"\nThe {river} runs through {countries_str}.")
#3: Name of every River in the Dictionary
print("\nRivers:")
for river in rivers.keys():
    print(river)
#4: Name of every Country in the Dictionary; in order alphabetically
print("\nCountries:")
all_countries = []
for value in rivers.values():
    for country in value:
        all_countries.append(country)
all_countries.sort()
for country in all_countries:
    print(country)

#END of RIVERS Program