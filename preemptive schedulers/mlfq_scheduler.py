'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
mflq_scheduler.py
'''


class MLFQScheduler:
    def __init__(self, scheduler1, scheduler2, scheduler3):
        self.schedulers = {1: scheduler1, 2: scheduler2, 3: scheduler3}

    def pick_process(self, ready, queue_level=1):
        queue = []

        # loop through and find the processes of the desired queue level,
        # if there are none, increase the queue level and try again.
        for process in ready:
            if process.get_queue_number() == queue_level:
                queue.append(process)
        if len(queue) == 0:
            return self.pick_process(ready, queue_level + 1)
        else:
            return self.schedulers[queue_level].pick_process(queue)

    def process_condition(self, process, start_time, time, ready):
        '''Here, we call the process condition of whatever queue we are on.'''
        return self.schedulers[process.get_queue_number()].process_condition(process, start_time, time, ready)
