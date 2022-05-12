'''
Eduardo Sosa
Project 09 - Disk Schedulers
May 6th, 2022
CS3337 - look.py
'''

import copy
import time


class Look_DScheduler:
    # initializes the look scheduler, takes in head and queue
    # list, sets seek time to 0 and begins the order.
    # the max is 200, which is the max of the disk
    def __init__(self, queue, head, max=200):
        self.head = head
        self.queue = queue
        self.seek_time = 0
        self.max = max
        self.order = [self.head]

    # clears the scheduler
    def clear(self, queue, head):
        self.seek_time = 0
        self.head = head
        self.queue = queue
        self.order = [self.head]

    # scans right until the highest process by sorting, then returns
    # to the minimum and scans right again
    def scan_right(self, queue):
        queue.sort()
        maximum = queue[-1] + 1
        for i in range(self.head, maximum):
            if i in queue:
                try:
                    while True:
                        queue.remove(i)
                except ValueError:
                    pass
                self.order.append(i)
            if len(queue) == 0:
                break
        self.seek_time += maximum - self.head - 1
        self.head = maximum - 1
        minimum = queue[0]
        for i in range(maximum, queue[0], -1):
            if i in queue:
                queue.remove(i)
                self.order.append(i)
            if len(queue) == 0:
                break
        self.head = minimum
        self.order.append(minimum)
        self.seek_time += maximum - self.head - 1
        return queue

    # calls scan_right
    def execute(self):
        queue = copy.deepcopy(self.queue)
        queue = self.scan_right(queue)


# test function
def main():
    fs = Look_DScheduler([98, 183, 37, 122, 14, 124, 65, 67], 53)
    fs.execute()
    print(fs.seek_time, fs.head)


if __name__ == '__main__':
    main()
