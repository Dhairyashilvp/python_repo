# Project Name

Immich photos uploader

## Description

This project processes directories and uploads their contents using the `immich` command-line tool. It also logs the output and errors.

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the project directory:**

    ```bash
    cd project_folder
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables:**

    Create a `.env` file in the root directory with the following content:

    ```plaintext
    API_URL=http://192.168.0.1:22/api
    TOKEN=sZvudnrv7qqBi4uH0IKPneBGMzWd2ss
    ```

5. **Run the project:**

    ```bash
    python src/main.py
    ```

6. **Verify output:**

    Check the `log` directory inside the `src` folder for log files containing the output of the script.
