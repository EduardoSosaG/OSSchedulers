'''
Eduardo Sosa
Project 09 - Disk Schedulers
May 6th, 2022
CS3337 - sstf.py
'''

import copy


class SSTF_DScheduler:

    # initializes the sstf scheduler, takes in head and queue
    # list, sets seek time to 0 and begin the order.
    def __init__(self, queue, head):
        self.head = head
        self.queue = queue
        self.seek_time = 0
        self.order = [self.head]

    # clears the scheduler
    def clear(self, queue, head):
        self.seek_time = 0
        self.head = head
        self.queue = queue
        self.order = [self.head]

    # executes based on shortest job from head
    def execute(self):
        queue = copy.deepcopy(self.queue)
        min = float('inf')
        min_proc = None
        while len(queue) > 0:
            for proc in queue:
                dist = proc - self.head
                if abs(dist) < min:
                    min = abs(dist)
                    min_proc = proc
            self.seek_time += min
            self.head = min_proc
            self.order.append(min_proc)
            queue.remove(min_proc)
            min = float('inf')


# test function
def main():
    fs = SSTF_DScheduler([98, 183, 37, 122, 14, 124, 65, 67], 53)
    fs.execute()
    print(fs.seek_time, fs.head)


if __name__ == '__main__':
    main()
