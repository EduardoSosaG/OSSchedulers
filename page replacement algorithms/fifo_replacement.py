'''
Eduardo Sosa
April 20th, 2022
CS337 - Project 08
fifo_replacement.py
'''


class FIFOReplacement:

    # Initializes the number of frames.
    def __init__(self, frames=5):
        self.frames = frames

    # Evicts pages based on a first in first out basis.
    # Counts the number of page evicts and returns the number.
    def execute(self, reference):
        faults = 0
        stack = []
        for page in reference:
            if page not in stack:
                if len(stack) == self.frames:
                    stack.pop(0)
                stack.append(page)
                faults += 1
        return faults
