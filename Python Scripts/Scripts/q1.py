# Question 1:  How do you execute a shell command in Python and capture its output? (e.g., using subprocess.run())


import subprocess
import os

# Main function to perform the task in given question
def execute_Command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    print("OutPut: ", result.stdout)
    print("Error: ", result.stderr)

def execute(cmd):
    if os.name == "nt":
        # Run in PowerShell explicitly
        result = subprocess.run(["powershell", "-Command", cmd], shell=True)
    else:
        result = subprocess.run(cmd, shell=True)


#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Type your command According to your SYSTEM ===> ").strip()
        
        if cmd == '0':
            print("\n!!!!!!!! Exiting the script.")
            exit = True
        else:
            print("\nRunning Command... \n")
            execute_Command(cmd)

def main():
    execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()