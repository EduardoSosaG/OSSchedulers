'''
Eduardo Sosa
CS337 - Project 01
February 16th, 2022
scheduler.py
'''
import random

def nonpreemptive_scheduler(scheduler_type, processes, ready, CPU, time, verbose = True):
    ''' non-preemptive FCFS scheduler '''

    # pick process depending on the scheduler type and assign it to the variable process
    if scheduler_type == 'fcfs':
        process = find_lowest_arrival(ready)
    elif scheduler_type == 'sjf':
        process = find_shortest_job(ready)
    elif scheduler_type == 'randomized_priority':
        process = random_priority(ready)
    else:
        process = find_highest_priority(ready)
    
    # set start time to time
    start_time = time    
    # while process is not finished
    while process.get_burst_time() > 0:
 
        # decrement process burst time by one
        process.set_burst_time(process.get_burst_time()-1)
        time+=1
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)
        
    end_time = time

    #remove the process from the ready-queue
    ready.remove(process)

    if scheduler_type == 'priority!':
        aging_priority(ready, time,end_time - start_time)

    #calculate turnaround time and wait time
    process.set_turnaround_time(end_time - process.get_arrival_time())
    process.set_wait_time(start_time - process.get_arrival_time())


    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Turnaround = process.get_turnaround_time(), 
                    WaitTime = process.get_wait_time()))
    return time

def find_lowest_arrival(ready):
    process = ready[0]
    #loop through and find the process with the lowest arrival time in the queue
    for i in range(1, len(ready)):
        if ready[i].get_arrival_time() < process.get_arrival_time():
            process = ready[i]
    return process

def find_shortest_job(ready):
    process = ready[0]
    #loop through the ready-queue and find the process with the shortest burst time. 
    for i in range(1, len(ready)):
        if ready[i].get_burst_time() < process.get_burst_time():
            process = ready[i]
    return process

def find_highest_priority(ready):
    process = ready[0]
    #loop through and find the process with the highest priority in the ready-queue
    for i in range(1, len(ready)):
        if ready[i].get_priority() > process.get_priority():
            process = ready[i]
        elif ready[i].get_priority() == process.get_priority():
            if ready[i].get_arrival_time() < process.get_arrival_time():
                process = ready[i]
    return process


def add_ready(processes, ready, time):
    #loop through the processes and add the processes that are ready to be run by the CPU. 
    for process in processes:
        if process.get_arrival_time() == time:
            ready.append(process)

def aging_priority(ready, time, total_time):
    #loop through the ready-queue and add one to the priority for every time step they've been in the ready-queue
    for process in ready:
        #if they joined the ready-queue while the previous process was being run, calculate the correct aging
        if time - process.get_arrival_time() < total_time:
            process.set_priority(process.get_priority()+time-process.get_arrival_time())
        else:
            process.set_priority(process.get_priority()+total_time)
def random_priority(ready):
    total_priority = 0
    #loop through the ready-queue and sum up all of the priorities. 
    for process in ready:
        total_priority += process.get_priority()

    #pick a random number between 1 and the total_priority
    random_int = random.randint(1, total_priority)

    current_priority = 0
    #pick the process picked by the random number. 
    for process in ready:
        current_priority += process.get_priority()
        if current_priority >= random_int:
            return process
    return process

    