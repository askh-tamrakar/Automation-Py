from paramiko.auth_strategy import Password
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

def main():
    print("\nConnecting SHH server and executing Commands")
    print("\n~~~> Configure Your SSH server ===> \n")
    config = input("Entert your: Host (IP/Domain), Username, Password \n-->")
    
    host, user, password = config.split(',')

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
   
if __name__ == "__main__":
   main()
