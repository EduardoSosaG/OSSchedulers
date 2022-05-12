'''
Eduardo Sosa
CS337 - semaphore.py
April 12th, 2022
'''


import threading


class Semaphore:

    # Initializes the counter and uses the threading
    # Package to initialize a condition variable.
    def __init__(self, counter=1):
        self.counter = counter
        self.condition = threading.Condition()

    # Acquires the semaphore and decreases the counter by one
    # Sleeps a thread if the counter falls below 0
    def acquire(self):
        self.condition.acquire()
        self.counter -= 1
        if self.counter < 0:
            self.condition.wait()
        self.condition.release()

    # Releases the semaphore. Increments counter and wakes
    # Up a single thread.
    def release(self):
        self.condition.acquire()
        self.counter += 1
        self.condition.notify()
        self.condition.release()
