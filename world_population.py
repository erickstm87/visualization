import json
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if(pop_dict['Year'] == '2010'):
        try:
            country_name = pop_dict['Country Name']
            country_pop = int(float((pop_dict['Value'])))
            code = get_country_code(country_name)
        except:
            print('weird number')
        else:
            if(code):
                print(code + ': ' + str(country_pop))
            else:
                print('error: ' + country_name)