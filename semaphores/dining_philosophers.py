'''
Eduardo Sosa
CS337 - dining_philosophers.py
April 12th, 2022
'''


import threading
import time
import random
import semaphore


class DiningPhilosophers:

    # Initializes the count, which is the number
    # Of philosophers.
    def __init__(self, count=5):
        self.count = count

    # This should produce a deadlock. Simulates each of the
    # Philosophers getting a hold of a fork (semiphore)
    def dining(self, lock, philosopher, left, right):
        for i in range(self.count):

            print("P", philosopher, " is thinking...")
            time.sleep(random.uniform(0.2, 0.6))

            print("P", philosopher, " is taking left fork...")
            left.acquire()
            time.sleep(0.6)

            print("P", philosopher, " is taking right fork...")
            right.acquire()
            time.sleep(0.6)

            print("P", philosopher, " is eating...")
            time.sleep(random.uniform(0.1, 1.0))
            time.sleep(random.uniform(0.2, 0.6))

            right.release()
            print("P", philosopher, " dropped right fork...")

            left.release()
            print("P", philosopher, " dropped left fork...")

        print("P", philosopher, " is finished!")

    # The solution method below takes in a lock, a thread
    # The left and right semaphores.
    # Solves the deadlock problem by letting
    # The odd numbered philosophers pick up the left fork
    # First followed by the right fork. Vice versa for the even-numbered.
    def solution(self, lock, philosopher, left, right):
        for i in range(self.count):

            print("P", philosopher, " is thinking...")
            time.sleep(random.uniform(0.2, 0.6))

            if philosopher % 2 == 0:
                print("P", philosopher, " is taking right fork...")
                right.acquire()
                time.sleep(0.6)

                print("P", philosopher, " is taking left fork...")
                left.acquire()
                time.sleep(0.6)
            else:
                print("P", philosopher, " is taking left fork...")
                left.acquire()
                time.sleep(0.6)

                print("P", philosopher, " is taking right fork...")
                right.acquire()
                time.sleep(0.6)

            print("P", philosopher, " is eating...")
            time.sleep(random.uniform(0.1, 1.0))
            time.sleep(random.uniform(0.2, 0.6))

            right.release()
            print("P", philosopher, " dropped right fork...")

            left.release()
            print("P", philosopher, " dropped left fork...")

        print("P", philosopher, " is finished!")

    # Creates the threads, if solution = False, produce
    # Deadlock, otherwise, run solution. Creates n-threads
    # Followed by n semaphores.
    def create_threads(self, solution=False):
        if solution:
            func = self.solution
        else:
            func = self.dining

        lock = threading.Lock()
        semaphores = []
        for i in range(self.count):
            s = semaphore.Semaphore()
            semaphores.append(s)

        threads = []
        for i in range(self.count):
            left = semaphores[i]
            if i == 0:
                right = semaphores[-1]
            else:
                right = semaphores[i-1]
            t = threading.Thread(target=func, args=(lock, i, left, right, ))
            threads.append(t)

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
