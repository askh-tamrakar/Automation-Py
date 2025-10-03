# Question 8: How do you send an HTTP GET/POST request in Python? (using requests library) ?





# Main function to perform the task in given question
from Scripts import q4 as json_util
from Scripts import q1 as cmd_executor
import requests
import json

def fetch_data(url, method="GET", data=None):
    try:
        if method.upper() == "GET":
            req = requests.get(url)
        elif method.upper() == "POST":
            req = requests.post(url, data=data)
        else:
            print(f" Unsupported method: {method}")
            return

        try:
            parsed = req.json()
            print(f"\n{method} Response from {url}:\n")
            print(json.dumps(parsed, indent=4, sort_keys=True))

            json_util.save_config_to_file(parsed, "./results/requests.json")
            
        except ValueError:
            print(f"\n{method} Response (not JSON):\n")
            print(req.text)
            print(parsed)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\nInput 0 to go back to Menu")
        print("\n=== HTTP Request Tool ===")

        url = input("Enter URL (default: https://httpbin.org/get): \n~> ").strip() or "https://httpbin.org/get"
        if url == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
        
        method = input("\nChoose method [GET/POST] (default: GET): \n~> ").strip().upper() or "GET"
        if method == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
            
        data = None
        if method == "POST":
            raw_data = input("Enter POST data as key=value (comma separated, e.g. user=admin,pass=123): ").strip()
            if raw_data:
                try:
                    data = dict(item.split("=") for item in raw_data.split(","))
                except Exception:
                    print("Invalid POST data format. Sending raw string instead.")
                    data = raw_data

        fetch_data(url, method, data)

          

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
