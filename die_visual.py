from die import Die

from plotly.graph_objs import  Bar, Layout
from plotly import offline

die = Die(6)
#make rolls and remember results
results = []
for roll in range(1000):
    res = die.roll()
    results.append(res)

#analize results
frequencies = []
for value in range(1, die.num_sides+1):
    frq = results.count(value)
    frequencies.append(frq)

#vizualize results
x_values = list(range(1, die.num_sides+1))
data =[Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of result'}
my_layout = Layout(title="Results of rolling 1 D6 1000 times",
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout},filename='resources/d6.html')