# Question 12: How do you schedule a Python script to run at a specific time daily? 
# (using schedule module or cron + Python)





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import schedule
import time

def job():
    print("Running scheduled job...")

    schedule.every().day.at("10:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

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
