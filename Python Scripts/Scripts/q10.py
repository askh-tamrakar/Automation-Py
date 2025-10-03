# Question 10: How do you compress and extract files in Python? (using zipfile / tarfile)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import zipfile
import tarfile

def compress_zip():
    with zipfile.ZipFile("files.zip", "w") as z:
        z.write("sample.txt")
    print("Compressed to files.zip")

def extract_zip():
    with zipfile.ZipFile("files.zip", "r") as z:
        z.extractall("extracted_zip")
    print("Extracted files.zip")


#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        cmd = input("\n~~~> Give the file that is to be extracted :\n===> ").strip()
        
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
