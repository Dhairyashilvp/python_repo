# src/immich_handler.py
import os
import subprocess
from tqdm import tqdm
from utils import get_timestamp, log_message
from dotenv import load_dotenv

def run_immich_command(folder, log_file):
    try:
        load_dotenv()  # Load environment variables from .env file
        api_url = os.getenv("API_URL")
        token = os.getenv("TOKEN")
        
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
