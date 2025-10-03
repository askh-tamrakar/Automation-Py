# Question 11: Write a Python script to connect to a remote server via SSH and run commands. (using paramiko)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import paramiko

def ssh_command(host, user, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    ssh.close()

if __name__ == "__main__":
    ssh_command("127.0.0.1", "user", "password", "ls -l")



#==================================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Type Variable name OR leave Blank to list ALL ===> ").strip()
        
        if cmd == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        else:
            print("\nListing the Variable... \n")
            if len(sys.argv) > 1:
                read_env(sys.argv[1])
            else:
                read_env()

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
