'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
pp_scheduler.py
'''


class PPScheduler:

    def __init__(self, quantum=1):
        self.quantum = quantum

    def set_quantum(self, quantum):
        self.quantum = quantum

    def get_quantum(self):
        return self.quantum

    def pick_process(self, ready):

        # loop through and find the process with the highest priority.
        process = ready[0]
        for i in range(1, len(ready)):
            if ready[i].get_priority() > process.get_priority():
                process = ready[i]
            elif ready[i].get_priority() == process.get_priority():
                if ready[i].get_arrival_time() < process.get_arrival_time():
                    process = ready[i]
        return process

    def process_condition(self, process, start_time, time, ready):
        '''For PP, the process condition is whether the burst time is 0
        or whether there exists another process that has higher priority
        within the ready list'''

        if process.get_burst_time() == 0:
            return False
        if (start_time - time) % self.quantum == 0:
            for other_process in ready:
                if process.get_priority() < other_process.get_priority():
                    return False
        return True
