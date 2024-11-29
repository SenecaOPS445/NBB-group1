#!/usr/bin/env python3
#Authors : Aravind Ravi Kumar / Vimodh Shehan Perera

""" 
This script will print the CPU usage to the console in real time and it will send an alert and a notification if the CPU usage exceeds the threshold which is set to 80% 
"""

import os  # For executing system commands
import time  # For time-related functions
import sys  # For system-specific parameters and functions
import select  # For monitoring input


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


def notify_user(message):

   #Send a desktop notification.
    

    os.system(f'notify-send "CPU Usage Alert" "{message}"')


def monitor_cpu():

   
   #Continuously check CPU usage and notify if it exceeds the specified limit.
   #The monitoring continues until the user types "exit".

    cpu_limit = 80.0 #Threshold set to 80%
    print(f"Monitoring CPU usage with a threshold of {cpu_limit}% every 5 seconds.") #Displays when the script is run

    print('Type "exit" to terminate the monitoring.\n') #Displays when the script is run


    while True:

        # Get the current CPU usage

        current_usage = get_cpu_usage()

        print(f"Current CPU Usage: {current_usage:.2f}%") #Displays the current usage in console, in 2 decimals


        # Check if the usage exceeds the defined limit

        if current_usage >= cpu_limit:

            alert_message = f"ALERT: CPU usage has exceeded {cpu_limit}%! Current usage: {current_usage:.2f}%" #Alert to be shown if current usage goes above the threshold

            print(alert_message)  # Output the alert to the console

            notify_user(alert_message)  # Trigger a desktop notification


        # Check for user input to exit

        if sys.stdin in select.select([sys.stdin], [], [], 5)[0]: #Wait for 5seconds for user input while the loop is running

            user_input = input().strip().lower() #read input, remove any spaces and make it lowercase

            if user_input == "exit":

                print("CPU usage monitoring stopped.")

                break #Exits the while loop


def main():
 
    monitor_cpu()  # Call the monitoring function with the default CPU limit


if __name__ == "__main__":

    main()
