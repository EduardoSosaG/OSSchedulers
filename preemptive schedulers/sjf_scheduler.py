'''
Eduardo Sosa
CS337 - Project 02
February 16th, 2022
process.py
'''


class SJFScheduler:

    def pick_process(self, ready):
        '''picks process according to which process has the
        lower burst time.'''

        process = ready[0]

        # loop through the ready-queue and find the process
        # with the shortest burst time.

        for i in range(1, len(ready)):
            if ready[i].get_burst_time() < process.get_burst_time():
                process = ready[i]
        return process
