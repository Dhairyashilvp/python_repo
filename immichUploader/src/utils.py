# src/utils.py
import os
import datetime
import subprocess
import shutil

from tqdm import tqdm

def get_log_file(type):
    log_dir = os.path.join(os.path.dirname(__file__), "log")
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, f"{type}_{get_timestamp()}.log")

def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def log_message(message, log_file):
    timestamp = get_timestamp()
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {message}\n")
    print(message)

def is_folder_empty(folder, err_log):
    try:
        return not any(os.scandir(folder))
    except Exception as e:
        error_message = f"Error checking if folder '{folder}' is empty: {str(e)}"
        log_message(error_message, err_log)

def immich_login(api_url, token, log_file):
    try:
        immich_path = shutil.which("immich")
        if immich_path is None:
            raise FileNotFoundError("The 'immich' command is not found in the system PATH.")
        
        command = [immich_path, "login", api_url, token]
        log_message(f"Login Command: {command}", log_file)
        
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Log standard output line by line
        for line in tqdm(iter(process.stdout.readline, ''), desc="Logging in", unit="line"):
            log_message(line.strip(), log_file)
        process.stdout.close()
        return_code = process.wait()
        # Log standard error
        for line in process.stderr:
            log_message(line.strip(), log_file)
        
        log_message(f"Process return code: {return_code}", log_file)
        
        if return_code != 0:
            raise subprocess.CalledProcessError(return_code, command)
            
    except FileNotFoundError as fnf_error:
        log_message(f"FileNotFoundError: {fnf_error}", log_file)
        exit()
    except subprocess.CalledProcessError as cpe:
        log_message(f"CalledProcessError: {cpe}", log_file)
        exit()
    except Exception as e:
        log_message(f"Unexpected error occurred during login: {str(e)}", log_file)
        exit()