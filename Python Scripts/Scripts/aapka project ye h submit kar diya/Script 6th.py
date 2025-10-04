import psutil
import platform
from time import sleep

def disk_usage():
    system = platform.system()

    if system == "Windows":
        usage = psutil.disk_usage("C:\\")
        percent = usage.percent
    else:
        usage = psutil.disk_usage("/")
        percent = usage.percent
    
    return percent

def main():
    print("\nStarting disk monitor... (logs every minute)\n")
    usage = disk_usage()

    if usage > 80:
        print(f"!!! ALERT: Disk usage is at {usage}% \n")
    else:
        print(f"Disk usage is at {usage}% - Chill within safe limits.")
    sleep(60)
   
if __name__ == "__main__":
   main()
