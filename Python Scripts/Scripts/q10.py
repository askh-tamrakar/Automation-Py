# Question 10: How do you compress and extract files in Python? (using zipfile / tarfile)?





# Main function to perform the task in given question
from Scripts import q1 as cmd_executor
import zipfile
import os

def compress_zip(files, output_zip=""):  
    """Compress files into a ZIP archive."""

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip:
        for file in files:
            if os.path.exists(file):
                zip.write(file, os.path.basename(file))
                print(f"Added {file} to the {output_zip}")
            else:
                print(F"FIle not Found: {file}")
    print(f"\n Compressed to {output_zip}")

def extract_zip(zipFile_path, extract_to_dir="."):
    """Extract files from a ZIP archive."""

    if not os.path.exists(zipFile_path):
        print(f"ZIP file not found: {zipFile_path}")
        return
    
    folder_name = os.path.splitext(os.path.basename(zipFile_path))[0]
    extract_to_dir = os.path.join(extract_to_dir, folder_name)

    os.makedirs(extract_to_dir, exist_ok=True)

    with zipFile_path.ZipFile(zipFile_path, "r") as zip:
        zip.extractall(extract_to_dir)
        print(f"\n Extracted to /{extract_to_dir}")


#===================================================================================================================




# Helper function to run the script
def helper():
    exit = False

    while not exit:
        print("\n--> Compression / Decompression Tool <--")
        print("1. To Extract from Zip archive")
        print("2. To Compress into Zip archive")
        print("0. Exit")

        choice = input("\n===> Enter Your Choice: \n=>").strip()

        
        if choice == '0':
            print("\n!!!!!!!! Exiting the script. ")
            exit = True
            break

        elif choice == "1":
            files = input("\nEnter file paths (comma-separated): ").split(",")
            filies = [f.strip() for f in files if f.strip()]
            output_zip = input("Enter ZIP filename (default: archive.zip): ").strip() or "archive.zip"
            compress_zip(files, output_zip)

        elif choice == "2":
            zipFile_path = input("Enter path to the ZIP file: ").strip()
            extract_dir = input("Enter extract directory (default: ./extracted): ").strip() or "./extracted"
            os.makedirs(extract_dir, exist_ok=True)
            extract_zip(zipFile_path, extract_dir)

        else:
            print("\n!!!Please give a valid choice. Try again!!!\n")
        

def main():
    cmd_executor.execute("clear")
    helper()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
if __name__ == "__main__":
   main()
