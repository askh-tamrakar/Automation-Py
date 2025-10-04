import os

def read_env(var_name):
    print("\nListing the Variable... \n")
    try:
        if var_name:
            value = os.environ.get(var_name, "Not Found")
            print(f"{var_name} = {value}")
    except Exception as e:
        print("An Error Ocurred: {e}")


def main():
    print("Environment Variable Lister...")
    var = input("Give variable name: \n> ")
    read_env(var)
   
if __name__ == "__main__":
   main()
