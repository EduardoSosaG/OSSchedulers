'''
Eduardo Sosa
Project 09 - Disk Schedulers
May 6th, 2022
CS3337 - fcfs.py
'''


class FCFS_DScheduler:

    # initializes the fcfs scheduler, takes in head and queue
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

    def execute(self):
        for proc in self.queue:
            self.seek_time += abs(self.head - proc)
            self.head = proc
            self.order.append(proc)


# test function
def main():
    fs = FCFS_DScheduler([98, 183, 37, 122, 14, 124, 65, 67], 53)
    fs.execute()
    print(fs.seek_time, fs.head)


if __name__ == '__main__':
    main()
