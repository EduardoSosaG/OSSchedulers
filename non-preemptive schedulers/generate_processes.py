'''
Eduardo Sosa
CS337 - Project 01
February 16th, 2022
generate_processes.py
'''
import process

def processes(scheduler_type, quantity = 10):
    processes = []
    #if the scheduler is fcfs, generate a dataset that simulates the convoy effect
    if scheduler_type == 'fcfs':
        for i in range(quantity):
            if i%10 == 0:
                processes.append(process.Process(i, 10, i, 0))
            else:
                processes.append(process.Process(i, 1, i, 0))

    #if the selected scheduler is sjf, generate a dataset that simulates starvation
    elif scheduler_type == 'sjf':
         for i in range(quantity):
            if i%10 == 0:
                processes.append(process.Process(i, 10, 0, 10))
            else:
                processes.append(process.Process(i, 1, i-1, 0))  
                
    #if the selected scheduler is priority scheduling, generate a dataset that simulates both the convoy effect and starvation.      
    else:
         for i in range(quantity):
            if i>4:
                processes.append(process.Process(i, 10, i%5, i*10+1))
            else:
                processes.append(process.Process(i, 1, i%5, i + 1))  

    return processes