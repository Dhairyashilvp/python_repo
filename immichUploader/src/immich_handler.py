# src/immich_handler.py
import os
import subprocess
import shutil
import time
from tqdm import tqdm
from utils import Utils
from dotenv import load_dotenv
class ImmichHandler:
    def __init__(self):
        load_dotenv()
        self.api_url = os.getenv("API_URL")
        self.token = os.getenv("TOKEN")
        self.time_ago = int(os.getenv("CREATED_HOURS_AGO")) * 60 * 60
        self.log_file = Utils.get_log_file("upload_log")
        self.err_log = Utils.get_log_file("error_log")
        self.immich_path = Utils.get_immich_path(self.err_log)

    def run_immich_command(self, folder_or_file):
        try:
            command = [self.immich_path, "upload", "--album", "--recursive", "--include-hidden", folder_or_file]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in tqdm(iter(process.stdout.readline, ''), desc=f"Uploading {folder_or_file}", unit="line"):
                Utils.log_message(line.strip(), self.log_file)
            process.stdout.close()
            process.wait()
            for line in process.stderr:
                Utils.log_message(line.strip(), self.log_file)
        except Exception as e:
            Utils.log_message(f"Error occurred while processing folder_or_file '{folder_or_file}': {str(e)}", self.err_log)
    
    def process_photos_folders(self, photo_dir):
        current_time = time.time()
        threshold_time = current_time - self.time_ago  # 72 hours in seconds

        for root, dirs, files in os.walk(photo_dir, topdown=False):  # Process nested subdirectories first
            if files and Utils.any_file_recent(root, files, threshold_time, self.err_log):
                # Utils.log_message(root, self.log_file)
                self.run_immich_command(root)

    
    def immich_login(self):
        try:
            Utils.log_message(f"API env details fetched API URL:{self.api_url} {self.token}",self.log_file)
            
            command = [self.immich_path, "login", self.api_url, self.token]
            Utils.log_message(f"Login Command: {command}", self.log_file)
            
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Log standard output line by line
            for line in tqdm(iter(process.stdout.readline, ''), desc="Logging in", unit="line"):
                Utils.log_message(line.strip(), self.log_file)
            process.stdout.close()
            return_code = process.wait()
            # Log standard error
            for line in process.stderr:
                Utils.log_message(line.strip(), self.log_file)
            
            # Utils.log_message(f"Process return code: {return_code}", self.log_file)
            
            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, command)
        except subprocess.CalledProcessError as cpe:
            Utils.log_message(f"Error occurred during login-CalledProcessError: {cpe}", self.err_log)
            exit()
        except Exception as e:
            Utils.log_message(f"Unexpected Error occurred during login: {str(e)}", self.err_log)
            exit()
    
    def immich_logout(self):
        try:
            command = [self.immich_path, "logout"]
            
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Log standard output line by line
            for line in tqdm(iter(process.stdout.readline, ''), desc="Logging out", unit="line"):
                Utils.log_message(line.strip(), self.log_file)
            process.stdout.close()
            return_code = process.wait()
            
            # Log standard error
            for line in process.stderr:
                Utils.log_message(line.strip(), self.log_file)
            
            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, command)
                
        except subprocess.CalledProcessError as cpe:
            Utils.log_message(f"Error occurred during logout-CalledProcessError: {cpe}", self.err_log)
            exit()
        except Exception as e:
            Utils.log_message(f"Unexpected Error occurred during logout: {str(e)}", self.err_log)
            exit()