import json
import yaml

def check_file(file):
    print("\nValidating the file....\n")
    try:
        if file.endswith(".json"):
            with open(file) as f:
                json.load(f)
        elif file.endswith(".yaml") or file.endswith(".yml"):
            with open(file) as f:
                yaml.safe_load(f)
        print(f"{file} is valid!")
    except Exception as e:
        print(f"{file} is INVALID: {e}")
        

def main():
    print("\nInput 0 to go back to Menu")
    file_path = input("\n~~~> Give path to a JSON or YAML file\n===> ").strip()
    check_file(file_path)

   
if __name__ == "__main__":
   main()
