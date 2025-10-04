# Question 17: How do you handle exceptions in Python while working with system commands?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import subprocess

def run_command(command):
    try:
        result = cmd_executor.execute(command)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Command failed:", e.stderr)



#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Type the Comman you want to execute:\n===> ").strip()
        
        if cmd == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        else:
            print("\nExecuting the Command... \n")
            run_command(cmd)


def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
