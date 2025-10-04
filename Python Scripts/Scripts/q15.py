# Question 15: How do you serialize and deserialize data in Python (JSON/YAML)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import json
import yaml

def serialize_deserialize(data, type='j', mode='s'):
    try:
        if type.lower() == 'j':
            if mode.lower() == 's':
                return json.dumps(data)

            elif mode.lower() == 'd':
                return json.loads(data)

            else:
                raise ValueError("Mode must be 's' for Serialize or 'd' for Deserialize.")

        elif type.lower() == 'y':
            if mode.lower() == 's':
                return yaml.dump(data)

            elif mode.lower() == 'd':
                return yaml.safe_load(data)

            else:
                raise ValueError("Mode must be 's' for Serialize or 'd' for Deserialize.")

        else:
            raise ValueError("Unsupported type. Use 'j' for JSON or 'y' for YAML.")

    except Exception as error:
        print (f"Error during {mode} operation: {error}")
        return None
    
#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        print("\n~~~> Choose File Type - JSON (j) or YAML (y), \and Mode - Serialize (s) or Deserialize (d): ")
        user = input("=> ").strip().lower()

        if user == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True

        file, mode = user.split(',')

        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
