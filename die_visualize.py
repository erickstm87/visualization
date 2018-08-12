import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for rolls in range(50000):
    result = die_1.roll() + die_2.roll();
    results.append(result)

frequencies = []
max_results = die_1.sides + die_2.sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.x_labels = []
total_sides = die_1.sides + die_2.sides + 1
for i in range(2, total_sides):
    hist.x_labels.append(i)
hist.title = "Results of rolling two six sided die 1000 times"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Roll'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
