from die import Die

from plotly.graph_objs import  Bar, Layout
from plotly import offline

#create 2 D6
die1 = Die(6)
die2 = Die(10)
#make rolls and remember results
results = []
for roll in range(50_000):
    res = die1.roll()+die2.roll()
    results.append(res)

#analize results
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frq = results.count(value)
    frequencies.append(frq)

#vizualize results
x_values = list(range(2, max_result+1))
data =[Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result', 'dtick': 1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title="Results of rolling 1xD6 and 1xD10 50 000 times",
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout},filename='resources/1xD6&1xD10.html')