import subprocess

# Main function to perform the task in given question
def execute_Command(cmd):
    result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, shell=True, check=True)
    print("OutPut: ", result.stdout)
    print("Error: ", result.stderr)

def main():
    print("Command Execution --->")
    cmd = input("Give your command that you want to execute: \n> ")
    execute_Command(cmd)

if __name__ == "__main__":
   main()