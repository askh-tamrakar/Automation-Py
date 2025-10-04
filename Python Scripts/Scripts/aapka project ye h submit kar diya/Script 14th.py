import time

def read_logs(file):
    with open(file, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                print(line, end="")
            time.sleep(0.5)

def main():
    print("Real-Time Log file Reading...\n")
    file_path = input("Give path to your Log File: \n").strip()
    
    print("Reading logs from the file....\n")
    try:
        read_logs(file_path)
    except Exception as error:
        print(f"/nAn error occured: {error}")
   
if __name__ == "__main__":
   main()
