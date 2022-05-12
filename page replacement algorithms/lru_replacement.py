'''
Eduardo Sosa
April 20th, 2022
CS337 - Project 08
lru_replacement.py
'''


class LRUReplacement:

    # Initializes the number of frames.
    def __init__(self, frames=5):
        self.frames = frames

    # Kepps track of each page using a stack and keeps track
    # Of the page index at which a page was last requested.
    # Evicts the one used farthest back.
    def execute(self, reference):
        faults = 0
        stack = []
        last_used = []
        for i, page in enumerate(reference):

            if page not in stack:
                if len(stack) == self.frames:
                    lru = 0
                    for j in range(1, len(last_used)):
                        if last_used[j] < last_used[lru]:
                            lru = j
                    stack.pop(lru)
                    last_used.pop(lru)

                stack.append(page)
                last_used.append(i)
                faults += 1
            else:
                index = stack.index(page)
                last_used[index] = i

        return faults
