'''
Eduardo Sosa
CS337 - Project 06
April 5th, 2022
bakery_solution.py
'''

import time


class BakerySolution:

    # Initializes the choosings and the tickets lists.
    def __init__(self, choosings, tickets):
        self.choosings = choosings
        self.tickets = tickets

    # The lock method follows the bakery lock
    # method from class.
    def lock(self, thread_id):
        self.choosings[thread_id] = True
        self.tickets[thread_id] = max(self.tickets)+1
        self.choosings[thread_id] = False

        time.sleep(0.0001)
        for p in range(len(self.tickets)):
            while(self.choosings[p]):
                pass
            while(self.tickets[p] != 0 and
                  (self.tickets[p] < self.tickets[thread_id] or
                  ((self.tickets[p] == self.tickets[thread_id]) and
                   (p < thread_id)))):
                pass

    # Releases the lock by changing the tickets index
    # of the id to 0.
    def unlock(self, thread_id):
        self.tickets[thread_id] = 0
