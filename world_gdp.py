import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

gdp_countries = {};
for pop_gdp in gdp_data:
    if(pop_gdp['Year'] == 2016):
        try:
            c_name = pop_gdp['Country Name']
            c_code = get_country_code(c_name)
            c_gdp = int(float(pop_gdp['Value']))
        except:
            print('couldn\'t find')
        else:
            if(c_code):
                gdp_countries[c_code] = c_gdp
            else:
                print('no code')

gdp_1, gdp_2, gdp_3 = {}, {}, {}
temp = []
for cc, gdp in gdp_countries.items():
    temp.append(gdp)
    if(gdp > 10000000000):
        gdp_1[cc] = gdp
    elif(gdp < 10000000000):
        gdp_2[cc] = gdp
    else:
        gdp_3[cc] = gdp
print(min(temp))
wm = pygal.maps.world.World()
wm.title = ('gdp in 2016')
wm.add('0-10b', gdp_2)
wm.add('>10b', gdp_1)
wm.add('10b', gdp_3)
wm.render_to_file('world_gdp.svg')
