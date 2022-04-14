'''
Eduardo Sosa
CS337 - Project 06
April 5th, 2022
solution_two.py
'''

import time


class SolutionTwo:

    # Initializes the flag variables to false.
    def __init__(self, flags=[False, False]):
        self.flags = flags

    # The lock method turns the flags to true if a thread is
    # going to access the critical method.
    def lock(self, thread_id):
        if thread_id == 1:
            self.flags[0] = True
            time.sleep(0.0001)
            while(self.flags[1]):
                pass
        if thread_id == 2:
            self.flags[1] = True
            time.sleep(0.0001)
            while(self.flags[0]):
                pass

    # Releases the lock by changing the the flags.
    def unlock(self, thread_id):
        if thread_id == 1:
            self.flags[0] = False
        else:
            self.flags[1] = False
