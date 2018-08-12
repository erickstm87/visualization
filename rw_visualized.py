import matplotlib.pyplot as plt
from randomWalk import RandomWalks

while True:
    rw = RandomWalks()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    # plt.plot(0, 0, c='green', s=100)
    # plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.show()

    keep_running = input('Take another walk? (y/n): ')
    if keep_running != 'y':
        break