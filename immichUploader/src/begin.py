from immich_handler import ImmichHandler

class Begin:
    @staticmethod
    def run(photo_directory):
        immich_handler = ImmichHandler()
        immich_handler.immich_login()
        immich_handler.process_photos_folders(photo_directory)
        immich_handler.immich_logout()
