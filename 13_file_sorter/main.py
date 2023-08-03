import os
import shutil


# BONUS: Create a tkinter app that allows the user to select the folder via a button

def create_folder(path: str, extension: str) -> str:
    """Creates a folder that is named after the extension of the file passed in"""

    # Create the folder name excluding the dot "."
    folder_name: str = extension[1:]

    # Create a valid path with the new folder name
    folder_path: str = os.path.join(path, folder_name)

    # If the folder path doesn't exist yet, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Return the new path
    return folder_path


def sort_files(source_path: str):
    """Sorts files based on a given path"""

    # Recursively walk through all the directories and files in the source path
    for root_dir, sub_dir, filenames in os.walk(source_path):

        # Get the full path for each file
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)

            # Splits the path into a root and the extension
            extension: str = os.path.splitext(filename)[1]

            # Check that there is an extension and create a folder if there is
            if extension:
                target_folder: str = create_folder(source_path, extension)

                # Create a path that leads to the target folder
                target_path: str = os.path.join(target_folder, filename)

                # Move the file from its current location to the target folder
                shutil.move(file_path, target_path)


def remove_empty_folders(source_path: str):
    """Removes all empty folders"""

    # We walk through all our folders again, but this time in a bottom-up approach
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):

        # Create a valid folder path for each dir
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)

            # Check if a folder is empty, and removes it if it is
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    # Get some user input
    user_input: str = input('Please provide a file path to sort: ')

    # Check if the path the user provided exists
    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
        print('Files sorted successfully!')
    else:
        print('Invalid path, please provide a valid file path.')


if __name__ == '__main__':
    main()
