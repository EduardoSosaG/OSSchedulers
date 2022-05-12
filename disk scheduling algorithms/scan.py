'''
Eduardo Sosa
Project 09 - Disk Schedulers
May 6th, 2022
CS3337 - scan.py
'''


import copy
import time


class Scan_DScheduler:

    # initializes the scan scheduler, takes in head and queue
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

    # scans left until 0
    def scan_left(self, queue):
        for i in range(self.head, -1, -1):
            if (i in queue):
                try:
                    while True:
                        queue.remove(i)
                except ValueError:
                    pass
                self.order.append(i)
            if len(queue) == 0:
                break
        self.seek_time += abs(self.head-i)
        self.head = 0
        self.order.append(0)
        return queue

    # scans right until the max
    def scan_right(self, queue):
        for i in range(self.head, self.max+1):
            if (i in queue):
                try:
                    while True:
                        queue.remove(i)
                except ValueError:
                    pass
                self.order.append(i)
            if len(queue) == 0:
                break
        self.seek_time += abs(self.head-i)
        self.head = self.max
        self.order.append(self.max)
        return queue

    # depending on the head and where it is,
    # we either scan left and then right or
    # vice versa
    def execute(self):
        queue = copy.deepcopy(self.queue)
        if self.head < (self.max/2):
            queue = self.scan_left(queue)
            queue = self.scan_right(queue)
        else:
            queue = self.scan_right(queue)
            queue = self.scan_left(queue)


# test function
def main():
    fs = Scan_DScheduler([98, 183, 37, 122, 14, 124, 65, 67], 53)
    fs.execute()
    print(fs.seek_time, fs.head)


if __name__ == '__main__':
    main()
