# src/main.py
import os
from immich_handler import process_folders
from dotenv import load_dotenv

def main():
    load_dotenv()  # Load environment variables from .env file
    root_directory = "E:\\Photos"  # Example directory
    process_folders(root_directory)

if __name__ == "__main__":
    main()
