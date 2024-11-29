#!/usr/bin/env python3
#Author: Aravind Kumar

import time


def get_cpu_usage():

   #Calculate CPU usage percentage from /proc/stat

    with open('/proc/stat', 'r') as file:    #Open the file in read mode
        cpu_times = list(map(int, file.readline().strip().split()[1:]))  #reads the first line, splits the line to seperate values, convert them to int and skip the word cpu
    
    idle_time = cpu_times[3] #Extracts the 4th value -idle time
    total_time = sum(cpu_times) #sums up all CPU time values

    time.sleep(1) #wait for 1second

    with open('/proc/stat', 'r') as file:
        cpu_times_next = list(map(int, file.readline().strip().split()[1:])) #reads the new CPU times
    
    return 100 * (1 - ((cpu_times_next[3] - idle_time) / (sum(cpu_times_next) - total_time)))  #Calculate % of the CPU usage



def main():
 
    monitor_cpu()  # Call the monitoring function with the default CPU limit

