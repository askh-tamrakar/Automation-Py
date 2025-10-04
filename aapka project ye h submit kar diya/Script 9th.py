import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Example Argparse Script")
    parser.add_argument("--name", required=True, help="Your name")
    parser.add_argument("--age", type=int, help="Your age")
    args = parser.parse_args()

    print(f"Hello {args.name}, Age: {args.age}")

def main():
    parse_arguments()
  
if __name__ == "__main__":
   main()
