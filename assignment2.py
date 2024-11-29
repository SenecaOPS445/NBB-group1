import os  # For executing system commands
import time  # For time-related functions
import argparse  # For handling command-line arguments
import sys  # For system-specific parameters and functions
import select  # For monitoring input


def get_cpu_usage():
    #Calculate CPU usage percentage from /proc/stat
    with open('/proc/stat', 'r') as file:
        cpu_times = list(map(int, file.readline().strip().split()[1:]))
    
    idle_time = cpu_times[3]
    total_time = sum(cpu_times)

    time.sleep(1)

    with open('/proc/stat', 'r') as file:
        cpu_times_next = list(map(int, file.readline().strip().split()[1:]))
    
    return 100 * (1 - ((cpu_times_next[3] - idle_time) / (sum(cpu_times_next) - total_time)))


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


def main():

    parser = argparse.ArgumentParser(description="Monitor CPU usage and alert if it exceeds a specified threshold.")

    parser.add_argument("--cpu_limit", type=float, default=80.0, help="Set the CPU usage threshold in percentage")

    args = parser.parse_args()

    monitor_cpu(cpu_limit=args.cpu_limit)


if __name__ == "__main__":

    main()
