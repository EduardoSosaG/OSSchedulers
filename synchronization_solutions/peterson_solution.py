'''
Eduardo Sosa
CS337 - Project 06
April 5th, 2022
peterson_solution.py
'''

import time


class PetersonSolution:

    # Initializes the flag variables into false and the turn into one.
    def __init__(self, flags=[False, False], turn=1):
        self.flags = flags
        self.turn = turn

    # The lock method changes the turn and the flags to True
    # depending on the thread about to access the critical section.
    def lock(self, thread_id):
        if thread_id == 1:
            self.flags[0] = True
            turn = 1
            time.sleep(0.0001)
            while(self.turn == 1 and self.flags[1]):
                pass
        if thread_id == 2:
            self.flags[1] = True
            turn = 0
            time.sleep(0.0001)
            while(self.turn == 0 and self.flags[0]):
                pass

    # Releases the lock by changing the flags.
    def unlock(self, thread_id):
        if thread_id == 1:
            self.flags[0] = False
        else:
            self.flags[1] = False
