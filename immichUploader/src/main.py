import sys
import os
from begin import Begin
from dotenv import load_dotenv

def main():
    load_dotenv()

    if len(sys.argv) > 2:
        print("Usage: python src/main.py [photo_directory]")
        sys.exit(1)
    
    if len(sys.argv) == 2:
        print(f"Processing arg dir {sys.argv[1]}")
        photo_directory = sys.argv[1]
    else:
        print(f"Processing env dir")
        photo_directory = os.getenv("PHOTO_DIRECTORY")

    if not photo_directory:
        print("Photo directory must be provided either as a command-line argument or in the .env file.")
        sys.exit(1)
        
    Begin.run(photo_directory)
    
if __name__ == "__main__":
    main()