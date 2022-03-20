'''
Eduardo Sosa
CS337 - Project 03
March 7th, 2022
scheduler.py
'''


def scheduler(scheduler_type, processes, ready, CPU, time, verbose=True):
    '''Chooses a process based on the scheduler type and then runs the process
    until the scheduler says so or the burst time runs to zero. Then we update
    the ready queue, wait time, response time and turnaround time. '''

    process = scheduler_type.pick_process(ready)

    # set start time to time
    start_time = time
    # while process follows the process condition set by the scheduler type
    while scheduler_type.process_condition(process, start_time, time, ready):

        # decrement process burst time by one
        process.set_burst_time(process.get_burst_time() - 1)

        time += 1
        # add processes that arrived now to ready queue
        scheduler_type.add_ready(processes, ready, time)

    end_time = time

    # if wait time is None, that means this is the first time this process
    # appears in the CPU, so we collect the response time.
    if process.get_wait_time() is None:
        process.set_response_time(start_time - process.get_arrival_time())
        process.set_wait_time(start_time - process.get_arrival_time())

    # else, update the wait time
    else:
        process.set_wait_time(start_time - process.get_arrival_time()
                              + process.get_wait_time())
    scheduler_type.update_ready_queue(ready, process, time, start_time)

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Turnaround=process.get_turnaround_time(),
                    WaitTime=process.get_wait_time(),
                    ResponseTime=process.get_response_time()))
    return time
