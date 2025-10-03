# Question 2: Write a Python script to check if a process is running on a Linux system. 

# If the process is not running, start it using a shell command.

# !!! I have made this script to work on both Linux and Windows systems. !!!


from Scripts import q1 as cmd_executor
import subprocess
import platform

# Main function to perform the task in given question
def check_process(process_name):
    system = platform.system() 

    try:
        # For Windows
        if system == "Windows":
            output = subprocess.check_output(["tasklist"], text=True)

            if process_name.lower() in output.lower():
                print(f"Process '{process_name}' is running.")
            else:
                print(f"Process '{process_name}' is NOT running.")
        
        # For Linux or Other
        else:
            output = subprocess.check_output(["pgrep", "-f", process_name])
            print(f"Process '{process_name}' is running with PID(s):\n{output.decode()}")
    
    except subprocess.CalledProcessError:
        print(f"Process '{process_name}' is NOT running.")

    

#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Type your process According to your SYSTEM ===> ").strip()
        
        if cmd == '0':
            print("\n!!!!!!!! Exiting the script.")
            exit = True
        else:
            print("\nChecking For Process... \n")
            check_process(cmd)

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
