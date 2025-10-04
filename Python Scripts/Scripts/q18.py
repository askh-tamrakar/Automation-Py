# Question 18: Write a Python script to generate a random password with letters, numbers, and symbols.





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    
    return password

#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\n<-- Password Generation Application -->")
        print("\nInput 0 to go back to Menu")
        length = input("\n~~~> Give the length of the password > 4 (default = 12):   ===> ").strip()
        
        if length == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        else:
            try:
                length = int(length) if length else 12
                if length < 4:
                    print("Password length should be at least 4.")
                    continue
                password = generate_password(length)
                print(f"\nGenerated Password: {password}\n")
            except ValueError:
                print("Please enter a valid number for length.")
            
        
def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
