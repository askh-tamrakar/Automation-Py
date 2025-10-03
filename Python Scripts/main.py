import importlib
from Scripts import q1 as cmd_executor

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


def run_script():
    print("<=== Python Utility Scripts ===>")

    for k in Scripts:
        print(f"{k}. Run script {k}")
    choice = input("\nEnter script number to run: ").strip()

    if choice in Scripts:
        module = importlib.import_module(Scripts[choice])

        if hasattr(module, "main"):
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            module.main() 
        else:
            print("This script runs standalone, not via main().")
    else:
        print("Invalid choice.")



def main():
    cmd_executor.execute("clear")
    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        run_script()
        reRun = input("\nDo you want to run another Script (y/n): ").strip().lower()

        if reRun != 'y':
            print("Exiting the script.")
            break
        

if __name__ == "__main__":
    main()
