# Question 15: How do you serialize and deserialize data in Python (JSON/YAML)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import os
import sys

def read_env(var_name=None):
    if var_name:
        value = os.environ.get(var_name, "Not Found")
        print(f"{var_name} = {value}")
    else:  # Read all environment variables
        for key, value in os.environ.items():
            print(f"{key} = {value}")


#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Type Variable name OR leave Blank to list ALL ===> ").strip()
        
        if cmd == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        else:
            print("\nListing the Variable... \n")
            if len(sys.argv) > 1:
                read_env(sys.argv[1])
            else:
                read_env()

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
