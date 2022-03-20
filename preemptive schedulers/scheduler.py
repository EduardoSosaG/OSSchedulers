'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
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
        add_ready(processes, ready, time)

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

    # gets the queue number before we update queue numbers.
    queue_number = process.get_queue_number()

    # updates the ready queue
    update_ready_queue(ready, process, time)

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    Turnaround=process.get_turnaround_time(),
                    WaitTime=process.get_wait_time(),
                    ResponseTime=process.get_response_time(),
                    QueueNumber=queue_number))
    return time


def add_ready(processes, ready, time):
    '''adds to ready and decrements io time for those waiting'''
    # loop through the processes and add the processes that are ready
    # to be run by the CPU.
    for process in processes:
        # if process is ready and running, add it to ready
        if process.get_arrival_time() == time and process.get_status() == 'running':
            ready.append(process)

        # else if process is waiting
        elif process.get_status() == 'waiting':

            # if it's done witing, set its burst time, arrival time, and status. Add to ready.
            if process.get_io_wait() == 0:
                ready.append(process)
                process.set_status('running')
                process.set_burst_time(process.get_duty()[2])
                process.set_arrival_time(time)

            # else, decrement the waiting time.
            else:
                process.decrement_io_wait()


def update_ready_queue(ready, process, time):
    '''updates the process in the ready queue such as queue number, arrival time, status,
    and removes the process.'''

    # if there's still burst time, change its queue number and set its arrival time to current time
    if process.get_burst_time() > 0:
        process.set_arrival_time(time)
        if process.get_queue_number() < 3:
            process.set_queue_number(process.get_queue_number() + 1)
    else:
        # remove the process from the ready-queue
        if process.get_io_wait() > 0:
            process.set_status('waiting')
            ready.remove(process)
        else:
            process.set_turnaround_time(process.get_duty()[0] + process.get_duty()[2]
                                        + process.get_wait_time())
            ready.remove(process)
