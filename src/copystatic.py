import shutil
import os

def copy_directory_contents(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for file in os.listdir(source):
        source_path = os.path.join(source, file)
        destination_path = os.path.join(destination, file)

        print(f" * {source_path} -> {destination_path}")

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            os.makedirs(destination_path)
            copy_directory_contents(source_path, destination_path)
