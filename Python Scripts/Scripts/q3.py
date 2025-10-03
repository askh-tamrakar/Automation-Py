# Question 3: How do you read environment variables in Python? (e.g., using os.environ)?

# edited the script so that we can add new environment variables as well as read existing ones.



# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import os

def read_write_env(var_name=None):
    if var_name.upper() == 'ADD':
        print("\nWriting the new Variable... \n")

        key = input("Enter Variable Name: ").strip()
        value = input("Enter Variable Value: ").strip()
        os.environ[key] = value
        print(f"Added: {key} = {value}")

    else:
        print("\nListing the Variable... \n")

        if var_name:
            value = os.environ.get(var_name, "Not Found")
            print(f"{var_name} = {value}")
        else:  
            for key, value in os.environ.items():
                print(f"=> {key} = {value}\n")


#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        var = input("\n~~~> Type Variable name OR leave Blank to list ALL... \n~~~> OR input ADD to write new one: \n=> ").strip()
        
        if var == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        else:
            if len(var) > 1:
                read_write_env(var)
            else:
                read_write_env()

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
