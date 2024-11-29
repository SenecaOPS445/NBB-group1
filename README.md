# Fall 2024 Assignment 2
#System Monitoring and Alerts
#Authors : Aravind Ravi Kumar / Vimodh Shehan Perera


1. How will your program gather required input?

- From the pre defined threshold which is 80%.
- User can input "exit" to stop the script from running.


2. How will your program accomplish its requirements?

- From reading CPU statistics from the /proc/stat file which provides detailed   CPU usage info in Linux machines
- Calculating CPU usage % by comparing idle time and total cpu time
- Checking if the CPU usage exceeds the threshold
- Triggering an alert if it does exceed. (Displays a warning message and sends a desktop notification using notify-send)



3. How will output be presented?

- The program will print the current CPU usage in real time in the console
- If CPU usage exceeds the threshold, an alert will be printed in the console and a desktop notification will be sent.


4. What arguments or options will be included?

- The script does not include any arguments or options. The CPU limit is fixed at 80%, and user interaction is limited to typing "exit" to terminate the program


5. What aspects of development do you think will present the most challenge?

- Real time CPU monitoring
- Notification handling

