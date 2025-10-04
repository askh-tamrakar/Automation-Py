import json

def load_config(file_path):
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
        

def save_config(config, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        print(f"\nCreated a JSON at '{file_path}' successfully.")

    except Exception as e:
        print(f"An error occurred while Creating JSON file: {e}")


        
        

def main():
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
            load_config(path)

    elif choice == "2":
            load_config(path)

    else:
        print("\n !!!Give a valid choice...\n")
   
if __name__ == "__main__":
   main()