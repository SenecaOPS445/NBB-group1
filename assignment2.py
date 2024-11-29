#!/usr/bin/env python3
#Author: Aravind Ravi Kumar
import time
import argparse

def get_cpu_usage():
    """Calculate CPU usage percentage from /proc/stat."""
    with open('/proc/stat', 'r') as file:
        cpu_times = list(map(int, file.readline().strip().split()[1:])) #the value is converted into integer and stored in the cpu_times
    
    idle_time = cpu_times[3]
    total_time = sum(cpu_times)

    time.sleep(1)

    with open('/proc/stat', 'r') as file:
        cpu_times_next = list(map(int, file.readline().strip().split()[1:]))
    
    return 100 * (1 - ((cpu_times_next[3] - idle_time) / (sum(cpu_times_next) - total_time)))

def main():
    """function to parse arguments and monitor CPU usage."""
    parser = argparse.ArgumentParser(description="Monitor CPU usage and alert if it exceeds provided threshold.")
    parser.add_argument("--cpu_limit", type=float, default=75.0, help="Set the CPU usage threshold in percentage")
    args = parser.parse_args()

    # current CPU usage
    current_usage = get_cpu_usage()
    print(f"The Current CPU Usage: {current_usage:.2f}%")

    #To check usage exceeds the limit
    if current_usage >= args.cpu_limit:
        print(f"Warning: The Usage Has Exeedeed {args.cpu_limit}%!!!!!!!")

if __name__ == "__main__":
    main()
