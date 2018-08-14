import json
import pygal
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
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
                cc_populations[code] = country_pop
            else:
                print('error: ' + country_name)

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010'
wm.add('North America', cc_populations)

wm.render_to_file('world_pop.svg')