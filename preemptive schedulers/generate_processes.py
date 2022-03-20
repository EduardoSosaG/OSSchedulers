'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
generate_processes.py
'''


import process
import random


def processes(quantity=1000):
    '''In this function, we generate the processes that will be
    used in our simulation'''

    # an array to store our processes
    processes = []
    for i in range(quantity):
        # pick an arrival time between 0 and 50
        arrival_time = random.randint(0, 50)

        # priority between 1 and 100
        priority = random.randint(1, 100)

        # here, we decide whether a process is IO or CPU bound
        if random.randint(0, 1):

            # allocates times for a CPU bound process
            cpu_time = random.randint(8, 12)
            io_time = random.randint(1, 3)
            first_cpu_time = random.randint(1, cpu_time-1)
            random_process = process.Process(i, [first_cpu_time, io_time,
                                             cpu_time - first_cpu_time],
                                             arrival_time, priority)
            processes.append(random_process)
        else:

            # allocates time for a io bound process
            cpu_time = random.randint(1, 2)
            io_time = random.randint(8, 12)
            random_process = process.Process(i, [cpu_time, io_time, 1],
                                             arrival_time, priority)
            processes.append(random_process)
    return processes
