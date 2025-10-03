# Question 16: Write a Python script to interact with AWS CLI or boto3 to list all S3 buckets.





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import boto3

def list_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
        print(bucket["Name"])

if __name__ == "__main__":
    list_buckets()



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
