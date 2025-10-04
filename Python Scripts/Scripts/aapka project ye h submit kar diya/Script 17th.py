import subprocess

def execute(cmd):
    try:
        result = subprocess.run(["powershell", "-Command", cmd], shell=True, check=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Command failed:", e.stderr)


def main():
    print("Exception Handler\n")
    cmd = input("Type the Comman you want to execute:\n> ").strip()

    print("\nExecuting the Command... \n")
    execute(cmd)

if __name__ == "__main__":
   main()
