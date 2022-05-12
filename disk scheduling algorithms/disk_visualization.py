'''
Eduardo Sosa
Project 09 - Disk Schedulers
May 6th, 2022
CS3337 - disk_visualization.py
'''


import matplotlib.pyplot as plt
import numpy as np
import fcfs
import sstf
import clook
import look
import scan
import cscan


# visualizes the order of the head pointer on the
# disks
def visualize(order):
    ax = plt.gca()
    ax.invert_yaxis()
    y = np.arange(len(order))
    plt.plot(order, y, marker="o")

    plt.show()


# main test function
def main():
    ds = scan.Scan_DScheduler([98, 183, 37, 122, 14, 124, 65, 67], 53)
    ds.execute()
    visualize(ds.order)


if __name__ == '__main__':
    main()
