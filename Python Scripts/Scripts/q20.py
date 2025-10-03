# Question 20: Write a Python script to validate a YAML/JSON configuration file for syntax errors.





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import json
import yaml

def validate_file(file):
    try:
        if file.endswith(".json"):
            with open(file) as f:
                json.load(f)
        elif file.endswith(".yaml") or file.endswith(".yml"):
            with open(file) as f:
                yaml.safe_load(f)
        print(f"{file} is valid!")
    except Exception as e:
        print(f"{file} is INVALID: {e}")

if __name__ == "__main__":
    validate_file("server_config.json")



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
        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
