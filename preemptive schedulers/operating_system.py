'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
operating_system.py
'''

import process
import scheduler
import pandas as pd


def kernel(processes, scheduler_type, verbose=True):
    '''Our kernel where we allocate our processes to the
    CPU according to our scheduler.'''
    CPU = []
    ready = []
    time = 0

    # for every process in processes, if the arrival time is equal to the time,
    # put it in the ready-queue
    for process in processes:
        if process.get_arrival_time() == time:
            ready.append(process)

    # while the ready-queue is nonempty, run the scheduler.
    while len(ready) > 0:
        time = scheduler.scheduler(scheduler_type, processes, ready, CPU, time)
    # calculates the average turnaround and the average wait by looping
    # through the processes
    avg_turnaround = 0
    avg_wait = 0
    avg_response = 0
    for process in processes:
        avg_turnaround += process.get_turnaround_time()
        avg_wait += process.get_wait_time()
        avg_response += process.get_response_time()
    avg_turnaround = avg_turnaround/len(processes)
    avg_wait = avg_wait/len(processes)
    avg_response = avg_response/len(processes)

    # save results as CSV, the averages go into a separate CSV file than
    # the processes dataframe
    df = pd.DataFrame(CPU)
    df2 = pd.DataFrame({'avg turnaround time': [avg_turnaround],
                        'avg wait time': [avg_wait],
                        'avg response time': [avg_response]})

    df.to_csv("results.csv", index=False)
    df2.to_csv("average_results.csv", index=False)
