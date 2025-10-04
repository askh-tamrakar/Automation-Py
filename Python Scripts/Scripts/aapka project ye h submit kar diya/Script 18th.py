from Scripts import q1 as cmd_executor
import random
import string

def Random_Str(len):
    chars = string.ascii_letters + string.digits + string.punctuation
    Random_Str = "".join(random.choice(chars) for _ in range(len))
    
    return Random_Str
           
        
def main():
    print("Password Generator")
    length = input("\nSet the length of Your Password: \n> ").strip()
    password = Random_Str(length)

    print(f"Your Random Password Is: \n> {password}")


if __name__ == "__main__":
   main()
