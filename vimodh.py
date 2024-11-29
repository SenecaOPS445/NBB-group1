#!/usr/bin/env python3
#Author: Vimodh Perera

import os 
import sys
import select

def notify_user(message):

    """
    Send a desktop notification using the `notify-send` command.
    """

    os.system(f'notify-send "CPU Usage Alert" "{message}"')


def monitor_cpu(cpu_limit):

    """

    Continuously check CPU usage and notify if it exceeds the specified limit.

    The monitoring continues until the user types "exit".

    """

    print(f"Monitoring CPU usage with a threshold of {cpu_limit}% every 5 seconds.")

    print('Type "exit" to terminate the monitoring.\n')


    while True:

        # Get the current CPU usage

        current_usage = get_cpu_usage()

        print(f"Current CPU Usage: {current_usage:.2f}%")


        # Check if the usage exceeds the defined limit

        if current_usage >= cpu_limit:

            alert_message = f"ALERT: CPU usage has exceeded {cpu_limit}%! Current usage: {current_usage:.2f}%"

            print(alert_message)  # Output the alert to the console

            notify_user(alert_message)  # Trigger a desktop notification


        # Check for user input to exit

        if sys.stdin in select.select([sys.stdin], [], [], 5)[0]:

            user_input = input().strip().lower()

            if user_input == "exit":

                print("CPU usage monitoring stopped.")

                break

