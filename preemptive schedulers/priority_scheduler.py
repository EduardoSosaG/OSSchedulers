'''
Eduardo Sosa
CS337 - Project 02
February 16th, 2022
process.py
'''


class PriorityScheduler:

    def pick_process(self, ready):
        process = ready[0]

        # loop through and find the process with the highest priority
        # in the ready-queue
        for i in range(1, len(ready)):
            if ready[i].get_priority() > process.get_priority():
                process = ready[i]
            elif ready[i].get_priority() == process.get_priority():
                if ready[i].get_arrival_time() < process.get_arrival_time():
                    process = ready[i]
        return process
