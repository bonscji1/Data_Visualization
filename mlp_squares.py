
import matplotlib.pyplot as plt

#choose style
plt.style.use('seaborn-dark')

fig, ax = plt.subplots()

x_values = range(1,1001)            #[1,2,3,4,5]
y_values = [x**2 for x in x_values] #[1,4,9,16,25]

#colormap cmap,c color,s size
ax.scatter(x_values,y_values,s=10,c=y_values,cmap=plt.cm.Greens)

ax.axis([0,1100,0,1100000])

#ax.scatter(2,4,s=200)

#input = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
#ax.plot(input, squares, linewidth=3)

#set chart title and label axes
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both',which='major',labelsize=14)

#plt.show()
plt.savefig("resources/test.png",bbox_inches='tight')
