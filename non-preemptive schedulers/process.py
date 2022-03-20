'''
Eduardo Sosa
CS337 - Project 01
February 16th, 2022
process.py
'''

class Process:

    #initializes all fields of the process object including ID, burst_time, arrival_time, and priority. 
    def __init__(self, id, burst_time, arrival_time, priority):
        self.id = id
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.wait_time = 0
        self.turnaround_time = 0
    
    #returns the process ID
    def get_ID(self):
        return self.id

    #returns the burst time
    def get_burst_time(self):
        return self.burst_time
    
    #returns the arrival time
    def get_arrival_time(self):
        return self.arrival_time
    
    #returns the priority
    def get_priority(self):
        return self.priority

    #returns the wait time
    def get_wait_time(self):
        return self.wait_time

    #returns the turnaround time
    def get_turnaround_time(self):
        return self.turnaround_time

    #sets the process burst time
    def set_burst_time(self, burst_time):
        self.burst_time = burst_time
    
    #sets the process arrival time
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time
    
    #sets the priority of the process
    def set_priority(self, priority):
        self.priority = priority

    #sets the process wait time
    def set_wait_time(self, wait_time):
        self.wait_time = wait_time

    #sets the process turnaround time
    def set_turnaround_time(self, turnaround_time):
        self.turnaround_time = turnaround_time
    

    