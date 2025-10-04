# Question 14: How can you write a Python script to read logs in real-time (like tail -f)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import time

def read_logs(file):
    with open(file, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                print(line, end="")
            time.sleep(0.5)

#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        file_path = input("\n~~~> Give path to your Log File ===> ").strip()
        
        if file_path == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        else:
            print("Reading logs from the file....")
            try:
                read_logs(file_path)
            except Exception as error:
                print(f"/nAn error occured: {error}")


        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
