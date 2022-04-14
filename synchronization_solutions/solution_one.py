'''
Eduardo Sosa
CS337 - Project 06
April 5th, 2022
solution_one.py
'''


class SolutionOne:

    # Initializes the turn variable
    def __init__(self, turn=1):
        self.turn = turn

    # The lock method checks if it's the threads turn
    def lock(self, thread_id):
        if thread_id == 1:
            while(self.turn != 1):
                pass
        if thread_id == 2:
            while(self.turn != 2):
                pass

    # Releases the lock by changing the turn.
    def unlock(self, thread_id):
        if thread_id == 1:
            self.turn = 2
        else:
            self.turn = 1
