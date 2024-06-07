# src/immich_handler.py
import os
import subprocess
import shutil
from tqdm import tqdm
from utils import get_timestamp, log_message, is_folder_empty, immich_login, get_log_file
from dotenv import load_dotenv

def run_immich_command(folder, log_file):
    try:
        immich_path = shutil.which("immich")
        if immich_path is None:
            raise FileNotFoundError("The 'immich' command is not found in the system PATH.")
        
        command = [immich_path, "upload", "--album", "--recursive", folder]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in tqdm(iter(process.stdout.readline, ''), desc=f"Uploading {folder}", unit="line"):
            log_message(line.strip(), log_file)
        process.stdout.close()
        process.wait()
        for line in process.stderr:
            log_message(line.strip(), log_file)
    except Exception as e:
        log_message(f"Error occurred while processing folder '{folder}': {str(e)}", log_file)

def process_folders(root_dir):
    log_file = get_log_file("upload_log")
    err_log = get_log_file("error_log")
    
    try:
        load_dotenv()  # Load environment variables from .env file
        api_url = os.getenv("API_URL")
        token = os.getenv("TOKEN")
        log_message(f"API env details fetched API URL:{api_url} {token}",log_file)
        immich_login(api_url, token, log_file)
    except Exception as e:
        log_message(f"Error occurred during login: {str(e)}", err_log)
        return
    
    for root, dirs, _ in os.walk(root_dir, topdown=False):  # Process nested subdirectories first
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not is_folder_empty(folder_path, err_log):
                run_immich_command(folder_path, log_file)
