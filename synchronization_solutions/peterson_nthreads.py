'''
Eduardo Sosa
CS337 - Project 06
April 5th, 2022
peterson_nthreads.py
'''

import time


class PetersonNThreads:

    # Initializes the flags variable list and the
    # last to enter list.
    def __init__(self, flags, last_to_enter):
        self.flags = flags
        self.last_to_enter = last_to_enter

    # The lock method follows the algorithm for peterson n-threads
    # found on wikipedia
    def lock(self, thread_id):

        for l in range(0, len(self.flags)-1):
            self.flags[thread_id] = l
            self.last_to_enter[l] = thread_id
            time.sleep(0.0001)
            while (self.last_to_enter[l] == thread_id and
                   self.higher_level(thread_id, l)):
                pass

    # Helper method for the lock method.
    def higher_level(self, thread_id, l):
        for i, thread in enumerate(self.flags):
            if self.flags[i] >= l and i != thread_id:
                return True
        return False

    # Releases the lock by changing the flag to -1.
    def unlock(self, thread_id):
        self.flags[thread_id] = -1
