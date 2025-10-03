# Question 9: Write a Python function to parse command-line arguments. (using argparse)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Example Argparse Script")
    parser.add_argument("--name", required=True, help="Your name")
    parser.add_argument("--age", type=int, help="Your age")
    parser.add_argument("-h", "--host", )
    args = parser.parse_args()

    print(f"Hello {args.name}, Age: {args.age}")


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
    parse_arguments()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
