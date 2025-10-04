import logging
import os

def setup_logger(log_file):
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

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


def main():
    exit = False
    name = ""
    msg = ""

    while not exit:
        print("\nLogging Application Started")

        while not exit:
            name = input("\nGive name to you log file (with .log extension) \n===> ").strip()
            
            if not name.endswith('.log'):
                print("\nPlease provide a valid log file name with .log extension.")
            else:
                break
        
        print("\nType 'END' to writing and save the file.")
        while True:
            msg = input("\n=> ").strip()


            if msg.strip().upper() == "END":
                print("Application exited\n")
                break

            elif not msg:
                print("\nPlease type a log message.")
                
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

if __name__ == "__main__":
   main()
