# Question 13:  Write a Python script to send an email alert when CPU usage is high.





# Main function to perform the task in given question
from email.mime.text import MIMEText
from Scripts import q1 as cmd_executor
import psutil
import smtplib

def send_email_alert():
    msg = MIMEText("High CPU Usage Detected!")
    msg["Subject"] = "ALERT: CPU Usage"
    msg["From"] = "you@example.com"
    msg["To"] = "admin@example.com"

    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)

def check_cpu():
    if psutil.cpu_percent(1) > 80:
        send_email_alert()

if __name__ == "__main__":
    check_cpu()



#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Type Variable name OR leave Blank to list ALL ===> ").strip()
        
        if cmd == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
