# Question 15: How do you serialize and deserialize data in Python (JSON/YAML)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import json
import yaml

data = {"name": "Alice", "age": 30}

# JSON
json_str = json.dumps(data)
print("JSON Serialized:", json_str)
print("JSON Deserialized:", json.loads(json_str))

# YAML
yaml_str = yaml.dump(data)
print("YAML Serialized:", yaml_str)
print("YAML Deserialized:", yaml.safe_load(yaml_str))



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
