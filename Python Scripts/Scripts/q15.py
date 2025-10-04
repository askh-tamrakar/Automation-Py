# Question 15: How do you serialize and deserialize data in Python (JSON/YAML)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
from pathlib import Path
import json
import yaml

def serialize_deserialize(data_file, Format='j', mode='s'):
    try:
        data_file = Path(data_file)

        if mode.lower() == 's':
            output_folder = Path("./Results/serialized_data")
        else:
            output_folder = Path("./Results/deserialized_data")

        output_folder.mkdir(parents=True, exist_ok=True)
        output_file = output_folder / data_file.name

        if mode.lower() == 's':
            if isinstance(data_file, Path):
                with open(data_file, "r", encoding="utf-8") as f:
                    data = eval(f.read()) 

            if format.lower() == 'j':
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
                return json.dumps(data)

            elif format.lower() == 'y':
                with open(output_file, "w", encoding="utf-8") as f:
                    yaml.dump(data, f)
                return yaml.dump(data)
            else:
                raise ValueError("Format must be 'j' (JSON) or 'y' (YAML).")

        elif mode.lower() == 'd':
            if format.lower() == 'j':
                with open(data_file, "r", encoding="utf-8") as f:
                    return json.load(f)

            elif format.lower() == 'y':
                with open(data_file, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f)

        else:
            raise ValueError("Mode must be 's' (serialize) or 'd' (deserialize).")

    except Exception as error:
        print (f"Error during {mode} operation: {error}")
        return None
    
#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        print("\n~~~> Choose File Type - JSON (j) or YAML (y), \n and Mode - Serialize (s) or Deserialize (d): ")
        user = input("=> ").strip().lower()

        if user == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
            return

        format_of_file, mode = user.split(',')

        path_to_data = input("\n~~~> Enter path to the Data File: ").strip()

        if path_to_data == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
            return
        else:
            result = serialize_deserialize(path_to_data, format_of_file.strip(), mode.strip())
            if result is not None:
                print(f"\nOperation successful. Result:\n{result}")
            else:
                print("\nOperation failed. Please check the inputs and try again.")


        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
