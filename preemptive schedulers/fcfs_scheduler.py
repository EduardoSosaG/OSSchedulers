'''
Eduardo Sosa
CS337 - Project 02
February 16th, 2022
process.py
'''


class FCFSScheduler:

    def pick_process(self, ready):
        '''picks the process for the FCFS scheduler. Looks at lowest arrival
        time and if two processes have the same arrival time, we take the
        process with the higher priority'''

        process = ready[0]
        # loop through and find the process with the lowest arrival time
        # in the queue
        for i in range(1, len(ready)):
            if ready[i].get_arrival_time() < process.get_arrival_time():
                process = ready[i]
        return process

    def process_condition(self, process, start_time, time, ready):
        '''evaluates whether the current process should be executed by the
        CPU. For fcfs, we simply check if the burst time has reached zero,
        otherwise we return True.'''

        if process.get_burst_time() == 0:
            return False
        return True
