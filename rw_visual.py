import matplotlib.pyplot as plt

from random_walk import RandomWalk

#random map generator :D
while True:
    #make random walk
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)

    plt.show()

    keep_runnin = input("Make another? (y/n):")
    if keep_runnin == 'n': break