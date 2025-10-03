# Question 5: How do you write logs to a file in Python with timestamps? (using logging module)





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import logging
import os

def setup_logger(log_file):
    """
    Sets up a logger for the given file.
    """
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger

def log(name, message, type='i'):
    log_file = os.path.join("./Results", name)
    logger = setup_logger(log_file)

    if type.lower() == 'w':
        logger.warning(message)
    elif type.lower() == 'e':
        logger.error(message)
    elif type.lower() == 'd':
        logger.debug(message)
    else:
        logger.info(message)

#=================================================================================================================================





# Helper function to run the script
def helper():
    exit = False
    name = ""
    msg = ""

    while not exit:
        print("Input 0 to go back to Menu")
        print("\nLogging Application Started")

        while not exit:
            name = input("\n~~~> Type your log file name (with .log extension) \n===> ").strip()
            if name == '0':
                exit = True
                break

            if not name.endswith('.log'):
                print("\nPlease provide a valid log file name with .log extension.")
            else:
                break
        
        print("\n~~~> Type your log message OR leave blank to see instructions: ")
        print("~~~> Type 'END' to stop logging messages and save the file.")
        while not exit:

            msg = input("\n=> ").strip()
            if msg == '0':
                print("\n!!!!!!!! Exiting the script. ")
                exit = True
                break

            elif msg.strip().upper() == "END":
                print("Application exited\n")
                break

            elif not msg:
                print("\nPlease type a log message. Example: 'This is a log message'")
                
            else:
                log(name, msg)

                while True:

                    msg = input("=> ").strip()
                    if msg.strip().upper() == "END":

                        if msg == 0:
                            exit = True
                        break

                    else:
                        log(name, msg)
        
                print(f"\nAll Log messages written to {name}")
                print("Application exited\n")
                break



def main():
   cmd_executor.execute("clear")
   helper()
   print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
   main()
