'''
Eduardo Sosa
April 20th, 2022
CS337 - Project 08
optimal_replacement.py
'''


class OPTReplacement:

    # Initializes the number of frames.
    def __init__(self, frames=5):
        self.frames = frames

    # Optimal algorithm and is not online.
    # Looks farthest into the future and determines
    # Page on stack with the farthest next request time
    # Evicts such pagea and returns faults.
    def execute(self, reference):
        faults = 0
        stack = []
        for i, page in enumerate(reference):

            if page not in stack:
                if len(stack) == self.frames:
                    seen = {}
                    farthest = stack[0]
                    for j in range(i+1, len(reference)):
                        if reference[j] not in seen and reference[j] in stack:
                            seen[reference[j]] = 1
                            farthest = reference[j]
                    for k in range(len(stack)):
                        if stack[k] not in seen:
                            farthest = stack[k]

                    stack.remove(farthest)

                stack.append(page)
                faults += 1

        return faults
