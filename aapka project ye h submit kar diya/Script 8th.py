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
            
        except ValueError:
            print(f"\n{method} Response (not JSON):\n")
            print(req.text)
            print(parsed)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


def main():
    print("GET/POST Application\n")

    url = input("Enter URL (default: https://httpbin.org/get): \n~> ").strip() or "https://httpbin.org/get"

    method = input("\nChoose method [GET/POST] (default: GET): \n~> ").strip().upper() or "GET"
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
   
if __name__ == "__main__":
   main()
