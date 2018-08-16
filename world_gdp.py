import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code

filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

gdp_countries = {};
for pop_gdp in pop_data:
    if(pop_gdp['Year'] == 2016):
        print(pop_gdp)