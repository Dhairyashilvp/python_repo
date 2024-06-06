# src/utils.py
import os
import datetime

def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def log_message(message, log_file):
    timestamp = get_timestamp()
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {message}\n")
    print(message)
