# src/begin.py

from immich_handler import ImmichHandler


class Begin:
    def run():
        immich_handler = ImmichHandler()
        immich_handler.immich_login()
        photo_directory = "E:\\Photos"  # Example directory
        immich_handler.process_photos_folders(photo_directory)
        immich_handler.immich_logout()