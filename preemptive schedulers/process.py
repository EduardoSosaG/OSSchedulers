'''
Eduardo Sosa
CS337 - Project 02
February 24th, 2022
process.py
'''


class Process:

    # initializes all fields of the process object including ID,
    # burst_time, arrival_time, and priority.
    def __init__(self, id, duty, arrival_time, priority):
        self.id = id
        self.duty = duty
        self.arrival_time = arrival_time
        self.priority = priority
        self.turnaround_time = 0
        self.response_time = 0
        self.status = 'running'
        self.io_wait = duty[1]
        self.burst_time = duty[0]
        self.queue_number = 1
        self.wait_time = None

    # returns the process ID
    def get_ID(self):
        return self.id

    # returns the io wait
    def get_io_wait(self):
        return self.io_wait

    # returns the duty
    def get_duty(self):
        return self.duty

    # returns burst time
    def get_burst_time(self):
        return self.burst_time

    # returns the arrival time
    def get_arrival_time(self):
        return self.arrival_time

    # returns the priority
    def get_priority(self):
        return self.priority

    # returns the wait time
    def get_wait_time(self):
        return self.wait_time

    # returns the turnaround time
    def get_turnaround_time(self):
        return self.turnaround_time

    # returns the response time
    def get_response_time(self):
        return self.response_time

    # returns the status
    def get_status(self):
        return self.status

    # returns the queue number
    def get_queue_number(self):
        return self.queue_number

    # sets the queue number
    def set_queue_number(self, number):
        self.queue_number = number

    # sets the status
    def set_status(self, status):
        self.status = status

    # sets the burst time
    def set_burst_time(self, time):
        self.burst_time = time

    # decrement the io wait
    def decrement_io_wait(self):
        self.io_wait -= 1

    # sets the response time
    def set_response_time(self, response_time):
        self.response_time = response_time

    # sets the process burst time
    def set_duty(self, duty):
        self.duty = duty

    # sets the process arrival time
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    # sets the priority of the process
    def set_priority(self, priority):
        self.priority = priority

    # sets the process wait time
    def set_wait_time(self, wait_time):
        self.wait_time = wait_time

    # sets the process turnaround time
    def set_turnaround_time(self, turnaround_time):
        self.turnaround_time = turnaround_time
