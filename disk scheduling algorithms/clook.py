'''
Eduardo Sosa
Project 09 - Disk Schedulers
May 6th, 2022
CS3337 - clook.py
'''


import copy
import time


class CLook_DScheduler:

    # initializes the clook scheduler, takes in head and queue
    # list, sets seek time to 0 and begins the order.
    # the max is 200, which is the max of the disk
    def __init__(self, queue, head, max=200):
        self.head = head
        self.queue = queue
        self.seek_time = 0
        self.order = [self.head]
        self.max = max

    # clears the scheduler
    def clear(self, queue, head):
        self.seek_time = 0
        self.head = head
        self.queue = queue
        self.order = [self.head]

    # scans right until the highest process by sorting, then returns
    # to 0 and scans right again.
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
        self.head = queue[0]
        self.seek_time += maximum - self.head - 1
        for proc in queue:
            self.seek_time += proc-self.head
            self.head = proc
            self.order.append(proc)
        return []

    # makes a deep copy of the queue and then calls scan right
    def execute(self):
        queue = copy.deepcopy(self.queue)
        queue = self.scan_right(queue)


# test function
def main():
    fs = CLook_DScheduler([98, 183, 37, 122, 14, 124, 65, 67], 53)
    fs.execute()
    print(fs.seek_time, fs.head)


if __name__ == '__main__':
    main()
