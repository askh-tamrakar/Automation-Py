import subprocess
import platform

def check_process(process_name):
    system = platform.system() 

    try:
        if system == "Windows":
            output = subprocess.check_output(["tasklist"], text=True)

            if process_name.lower() in output.lower():
                print(f"Process '{process_name}' is running.")
            else:
                print(f"Process '{process_name}' is NOT running.")
        
        else:
            output = subprocess.check_output(["pgrep", "-f", process_name])
            print(f"Process '{process_name}' is running with PID(s):\n{output.decode()}")
    
    except subprocess.CalledProcessError:
        print(f"Process '{process_name}' is NOT running.")


def main():
    print("\nInput 0 to go back to Menu")
    cmd = input("\n~~~> Type your process According to your SYSTEM ===> ").strip()
    
    print("\nChecking For Process... \n")
    check_process(cmd)
   
if __name__ == "__main__":
   main()
