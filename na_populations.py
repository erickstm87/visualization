import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of North America'
wm.add('North America', {'ca': 34126000, 'us': 30934900, 'mx': 113423000})

wm.render_to_file('na_pop.svg')