# Question 6: How can you monitor disk usage and alert if usage exceeds 80% using Python?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
from Scripts import q5 as logger_util 
from time import sleep
import psutil
import platform

def disk_usage():
    system = platform.system()

    if system == "Windows":
        usage = psutil.disk_usage("C:\\")
        percent = usage.percent
    else:
        usage = psutil.disk_usage("/")
        percent = usage.percent
    
    return percent

#===================================================================================================================

# Helper function to run the script
def helper():
    print("\nStarting disk monitor... (logs every minute)\n")
    log_file = "disk_usage.log"

    try:
        while True:
            msg = disk_usage()

            if msg > 80:
                logger_util.log(log_file, f"!!! ALERT: Disk usage is at {msg}% \n", 'w')
            else:
                logger_util.log(log_file, f"~>Disk usage is at {msg}% - within safe limits.\n")

            sleep(60)

    except KeyboardInterrupt:
        print("\n Disk Monitor is Stopped....")


def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
