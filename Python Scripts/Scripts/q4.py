# Question 4:  Write a Python script to parse a JSON file containing server configurations.




# Main function to perform the task in given question
from encodings import utf_16
from Scripts import q1 as cmd_executor
import json

def load_config_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        print("\nServer Configurations Loaded from File: \n")
        print("Server Configurations: \n", config)

    except FileNotFoundError:
        print(f"Error: FiJSONDecodeErrorle '{file_path}' not found.")

    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        


def load_config_from_input():
    
    print("\nEnter your JSON configuration directly (single line or multi-line).")
    print("Type 'END' on a new line when you're done: \n")
    
    config = {}
    while True:
        line = input("=> ")
        if line.strip().upper() == "END":
            break
        if "=" in line:
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    
    try:
        print("\nServer Configurations Loaded from Input:\n")
        with open("./results/Server_Config.json", "w") as f:
            print(json.dumps(config, indent=4))     
            print("!!! Saved configuration to server_config.json")

    except json.JSONDecodeError:
        print("\nInvalid JSON format in your input. Please try again.")

    return config



def save_config_to_file(config, file_path):
    """
    Save a Python dict to a JSON file.
    Ensures results folder exists.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        print(f"\nCreated a JSON at '{file_path}' successfully.")

    except Exception as e:
        print(f"An error occurred while Creating JSON file: {e}")


#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nOptions: ")
        print("1. Provide a file path to load JSON")
        print("2. Type JSON directly in console")
        print("0. Exit")
        
        choice = input("\n===> Enter your Choice: ").strip()

        if choice == "0":
            print("\n!!!!!!!! Exiting the script.")
            exit = True

        elif choice == "1":
            path = input("\n~~~> Enter path to the Server Config JSON file \n===> ").strip()

            if not path:
                print("!!! Please give a valid path")
            else:
                load_config_from_file(path)

        elif choice == "2":
                load_config_from_input()

        else:
            print("!!! Invalid choice, please try again.")
        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()