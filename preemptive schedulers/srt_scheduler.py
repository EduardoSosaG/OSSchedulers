'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
srt_scheduler.py
'''


class SRTScheduler:

    def __init__(self, quantum=1):
        self.quantum = quantum

    # sets the quantum
    def set_quantum(self, quantum):
        self.quantum = quantum

    # returns the quantum
    def get_quantum(self):
        return self.quantum

    def pick_process(self, ready):
        '''picks process according to which process has the
        lowest burst time'''

        process = ready[0]

        # loop through the ready-queue and find the process
        # with the shortest burst time.
        for i in range(1, len(ready)):
            if ready[i].get_burst_time() < process.get_burst_time():
                process = ready[i]
        return process

    def process_condition(self, process, start_time, time, ready):
        '''the process condition for the SRT scheduler is whether the
        burst time is zero or whether there is a process in
        the ready queue with a lowest burst time'''

        if process.get_burst_time() == 0:
            return False
        if (start_time - time) % self.quantum == 0:
            for other_process in ready:
                if other_process.get_burst_time() < process.get_burst_time():
                    return False
        return True
