import matplotlib.pyplot as plt

from random_walk import RandomWalk

#random map generator :D
while True:
    #make random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()


    #settings for graphs
    plt.style.use('seaborn-dark')
    small_point = 1
    big_point = 80

    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,
               s=small_point, c=point_numbers, cmap=plt.cm.Greens, edgecolors="none")

    #emphatize 1st and last poin
    ax.scatter(0,0,c="Blue",edgecolors="none",s=big_point)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=big_point)

    #remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_runnin = input("Make another? (y/n):")
    if keep_runnin == 'n': break