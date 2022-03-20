'''
Eduardo Sosa
CS337 - Project 03
March 7th, 2022
cfs_scheduler.py
'''

import math


class CFSScheduler:
    ''' This class implements the CFS Scheduler by defining a few terms
    (constructor) and then defining the process picking function, the
    process condition, the add ready, and the update ready queue methods.'''

    def __init__(self, target_latency):
        self.target_latency = target_latency
        self.dynamic_quantum = 0
        self.ready_processes = []

    def pick_process(self, ready):
        '''pick processes by first computing the dynamic quantum, then
        picking the process with the lowest vruntime and returning that
        process.'''

        self.dynamic_quantum = self.target_latency/ready.get_size()

        if self.dynamic_quantum < 1:
            self.dynamic_quantum = 1
        else:
            self.dynamic_quantum = math.floor(self.dynamic_quantum)

        # get the min vruntime process from rb tree.
        process = ready.get_min_vruntime().get_process()
        return process

    def process_condition(self, process, start_time, time, ready):
        ''' a process stays in condition if the dynamic quantum is
        zero or if the burst time is equal to zero.'''

        # check if dynamic quantum is zero
        if self.dynamic_quantum == 0:
            return False

        # check if burst time is zero.
        elif process.get_burst_time() == 0:
            return False
        else:
            # else, decrement the dynamic quantum by 1.
            self.dynamic_quantum -= 1
            return True

    def add_ready(self, processes, ready, time):
        '''adds to ready and decrements io time for those waiting'''
        # loop through the processes and add the processes that are ready
        # to be run by the CPU.
        for process in processes:
            # if process is ready and running, add it to ready
            if (process.get_arrival_time() == time and
                    process.get_status() == 'running'):
                self.ready_processes.append(process)

            # else if process is waiting
            elif process.get_status() == 'waiting':

                # if it's done witing, set its burst time, arrival time,
                # and status. Add to ready.
                if process.get_io_wait() == 0:
                    self.ready_processes.append(process)
                    process.set_status('running')
                    process.set_burst_time(process.get_duty()[2])
                    process.set_arrival_time(time)

                # else, decrement the waiting time.
                else:
                    process.decrement_io_wait()

    def update_ready_queue(self, ready, process, time, start_time):
        '''updates the process in the ready queue such as queue number,
        arrival time, status, and removes the process.'''

        # if there's still burst time, change its queue number and set
        # its arrival time to current time
        if process.get_burst_time() > 0:
            process.set_arrival_time(time)
            process.set_vruntime((time-start_time)*process.get_weight())
            ready.remove_min_vruntime()
            ready.append(process)
        else:
            # remove the process from the ready-queue
            if process.get_io_wait() > 0:
                process.set_status('waiting')
                process.set_vruntime((time-start_time)*process.get_weight())
                ready.remove_min_vruntime()
            else:
                process.set_turnaround_time(process.get_duty()[0]
                                            + process.get_duty()[2]
                                            + process.get_wait_time())
                ready.remove_min_vruntime()
        for process in self.ready_processes:
            ready.append(process)
        self.ready_processes = []
