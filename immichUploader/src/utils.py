# src/utils.py
import os
import datetime
import subprocess
import shutil
from tqdm import tqdm

class Utils:
    @staticmethod
    def get_log_file(type):
        log_dir = os.path.join(os.path.dirname(__file__), "log")
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{type}_{Utils.get_timestamp()}.log")

    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def log_message(message, log_file):
        timestamp = Utils.get_timestamp()
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {message}\n")
        print(message)

    @staticmethod
    def is_folder_empty(folder, err_log):
        try:
            return not any(os.scandir(folder))
        except Exception as e:
            error_message = f"Error checking if folder '{folder}' is empty: {str(e)}"
            Utils.log_message(error_message, err_log)

    @staticmethod
    def get_immich_path(err_log):
        try:
            immich_path = shutil.which("immich")
            if immich_path is None:
                raise FileNotFoundError("The 'immich' command is not found in the system PATH.")
            return immich_path
        except FileNotFoundError as fnf_error:
            Utils.log_message(f"Error occurred during logout-FileNotFoundError: {fnf_error}", err_log)
            exit()
