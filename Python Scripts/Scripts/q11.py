# Question 11: Write a Python script to connect to a remote server via SSH and run commands. (using paramiko)?





# Main function to perform the task in given question
from paramiko.auth_strategy import Password
from Scripts import q1 as cmd_executor
import paramiko

def ssh_connect(host, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    print("<-- Connection Successfull... -->")
    return ssh

def ssh_command(cmd, ssh):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())

def shut_server(ssh):
    ssh.close()

#==================================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        print("\n~~~> Give the credentials for your SSH server ===> \n")

        credentials = input("Entert your: Host (IP/Domain), Username, Password \n-->")

        host, user, password = credentials.split(',')

        if host == '0' or user == '0' or password == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True

        else:
            try:
                ssh = ssh_connect(host, user, password)
                while True:
                    command = input("\nEnter Command to execute: ").strip()
                    if command.lower() in ['exit', 'quit']:
                        print("\nExiting command execution.")
                        break
                    ssh_command(command, ssh)
                shut_server(ssh)
            except Exception as error:
                print(f"\nAn error occurred: {error}")

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
