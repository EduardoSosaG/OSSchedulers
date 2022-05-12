'''
Eduardo Sosa
April 20th, 2022
CS337 - Project 08
mfu_replacement.py
'''


class MFUReplacement:

    # Initializes the number of frames.
    def __init__(self, frames=5):
        self.frames = frames

    # Evicts pages based on the number of times the page
    # Has been requested. Evicts page requested the most.
    # Returns faults.
    def execute(self, reference):
        faults = 0
        stack = []
        used = []
        for i, page in enumerate(reference):

            if page not in stack:
                if len(stack) == self.frames:
                    lru = 0
                    for j in range(1, len(used)):
                        if used[j] > used[lru]:
                            lru = j
                    stack.pop(lru)
                    used.pop(lru)

                stack.append(page)
                used.append(1)
                faults += 1
            else:
                index = stack.index(page)
                used[index] += 1

        return faults
