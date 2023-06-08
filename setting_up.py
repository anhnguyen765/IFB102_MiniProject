# Import essential packages
import os

# Define a function to check if a file is exists
def create_directory():
    while True:
        directory = input("Register new username: ")
        parent_dir = "/home/pi/miniproject/Face_Recognition/dataset"
        dir_path = os.path.join(parent_dir, directory)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"New user with the name '{directory}' created")
            break
        else:
            print(f"The user '{directory}' already exists")
    return directory

