# src/main.py
import os
from immich_handler import run_immich_command,process_folders
from dotenv import load_dotenv

def main():
    root_directory = "E:\\Photos"  # Example directory
    process_folders(root_directory)

if __name__ == "__main__":
    main()
