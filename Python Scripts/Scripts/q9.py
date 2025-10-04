# Question 9: Write a Python function to parse command-line arguments. (using argparse)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor

import argparse
import sys

def get_arguments():
    """
    Parses command-line arguments and returns them as a dictionary.
    Other scripts can import and use this function.
    """

    parser = argparse.ArgumentParser(
        description="Command-line argument parser for Python Utility Scripts (1-20)."
    )

    parser.add_argument(
        "-s", "--script",
        type=str,
        help="Script number to run (1-20)."
    )

    args = parser.parse_args()

    return args.script


#===================================================================================================================


def main():
    """
    If q9.py is run directly, show a help demo.
    """
    cmd_executor.execute("clear")
    args = get_arguments()

    if not args or args == '9':
        print("\nExample usage:")
        print("   python main.py -s 5")
        sys.exit()

    print(f"Script selected: {args}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
