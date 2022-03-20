'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
rr_scheduler.py
'''


class RRScheduler:

    def __init__(self, quantum):
        self.quantum = quantum

    # sets the quantum
    def set_quantum(self, quantum):
        self.quantum = quantum

    # returns the quantum
    def get_quantum(self):
        return self.quantum

    def pick_process(self, ready):
        '''picks the process based on the process with the lowest arrival
        time and then tie breaks using priority number'''

        process = ready[0]

        # loop through and find the process with the lowest arrival
        # time in the queue
        for i in range(1, len(ready)):
            if ready[i].get_arrival_time() < process.get_arrival_time():
                process = ready[i]
            elif ready[i].get_arrival_time() == process.get_arrival_time():
                if ready[i].get_priority() > process.get_priority():
                    process = ready[i]
        return process

    def process_condition(self, process, start_time, time, ready):
        '''the process condition is whether the burst time has gone to zero or
        whether the process has used the cpu for the quantum time'''

        if time - start_time == self.quantum or process.get_burst_time() == 0:
            return False
        return True
