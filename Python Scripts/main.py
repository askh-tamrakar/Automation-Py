import importlib
from Scripts import q1 as cmd_executor
from Scripts import q9 as arg_parser

Scripts = {
    "1": "Scripts.q1",
    "2": "Scripts.q2",
    "3": "Scripts.q3",
    "4": "Scripts.q4",
    "5": "Scripts.q5",
    "6": "Scripts.q6",
    "7": "Scripts.q7",
    "8": "Scripts.q8",
    "9": "Scripts.q9",
    "10": "Scripts.q10",
    "11": "Scripts.q11",
    "12": "Scripts.q12",
    "13": "Scripts.q13",
    "14": "Scripts.q14",
    "15": "Scripts.q15",
    "16": "Scripts.q16",
    "17": "Scripts.q17",
    "18": "Scripts.q18",
    "19": "Scripts.q19",
    "20": "Scripts.q20"
}

print_title = [
    "Execute Shell Command and Capture it's OutPut",
    "Check Process is Running or Not",
    "Read Environment Variable",
    "Parse Server Configuration in JSON file",
    "Create a log file with TimpeStamp",
    "Monitor Disk Usage",
    "Check if a Port is Open on a Given Host",
    "Send HTTP GET/POST Request",
    "Prase Command Line Arguments",
    "Compress and Extract a Zip File",
    "Connect and Execute commands on SSH Server",
    "Schedule a Task Daily - X",
    "Send Alert Email of High CPU Usage - X",
    "Read Log File in Real Time",
    "Serialize and Deserialize JSON or YAML Data",
    "Lsit All S3 Buckets from AWS,CLI, or Boto3 - X",
    "Exception Handling when Executing a System Command",
    "Generate a Random Password",
    "Check Execution Time of a Script - X",
    "Validate JSON or YAML File Against a Schema"
]

def run_specific_script(script_number: str):   

    try:
        module = importlib.import_module(Scripts[script_number])
        if hasattr(module, "main"):
            module.main()
        else:
            print(f"{script_number} has no main() function.")

    except Exception as e:
        print(f"Error running {script_number}: {e}")


    args = arg_parser.get_arguments()

def run_script():
    print("<=== Python Utility Scripts ===>")

    column_width = max(len(title) for title in print_title) + 2

    print("-" * (column_width + 10))
    print(f"| {'No.':<3} | {'Fuction of Script'.ljust(column_width)} |")
    print("-" * (column_width + 10))

    for i, title in enumerate(print_title, start=1):
        print(f"| {i:<3} | {title.ljust(column_width)} |")
        print("-" * (column_width + 10))

    print("!!! X at the END of Title means the Scritpt is Under Development... Sorry for Inconvience")
    choice = input("\nEnter script number to run: ").strip()

    if choice in Scripts:
        module = importlib.import_module(Scripts[choice])

        try:
            if hasattr(module, "main"):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                module.main()
        except Exception as error:
            print(f"Error in Running Module: {error}")
    else:
        print("Invalid choice.")



def main():
    cmd_executor.execute("clear")
    args = arg_parser.get_arguments()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    if args:
        run_specific_script(args)
    else:
        while True:
            run_script()
            reRun = input("\nDo you want to run another Script (y/n): ").strip().lower()

            if reRun != 'y':
                print("Exiting the script.")
                break
        

if __name__ == "__main__":
    main()