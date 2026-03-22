import os
import shutil
import logging

# ----------------------------
# Setup logging
# ----------------------------
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# File type categories
# ----------------------------
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# ----------------------------
# Function to copy files to project Organized_Files
# ----------------------------
def organize_files(source_path, project_path):
    try:
        if not os.path.exists(source_path):
            print("Source path does not exist.")
            return

        # Create Organized_Files folder in project
        organized_folder = os.path.join(project_path, "Organized_Files")
        if not os.path.exists(organized_folder):
            os.makedirs(organized_folder)

        # If source_path is a file, make a list with just that file
        if os.path.isfile(source_path):
            files_to_process = [source_path]
        else:
            # List all files in folder
            files_to_process = [os.path.join(source_path, f) for f in os.listdir(source_path)
                                if os.path.isfile(os.path.join(source_path, f))]

        for file_path in files_to_process:
            file_name = os.path.basename(file_path)
            file_ext = os.path.splitext(file_name)[1].lower()
            moved = False

            # Find correct folder
            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    target_folder = os.path.join(organized_folder, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    target_path = os.path.join(target_folder, file_name)
                    if not os.path.exists(target_path):
                        shutil.copy2(file_path, target_path)  # Copy file
                        logging.info(f"Copied {file_name} to {folder_name}")
                    moved = True
                    break

            # Unknown file types go to Others
            if not moved:
                other_folder = os.path.join(organized_folder, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                target_path = os.path.join(other_folder, file_name)
                if not os.path.exists(target_path):
                    shutil.copy2(file_path, target_path)
                    logging.info(f"Copied {file_name} to Others")

        print(f"Files successfully added to {organized_folder}")

    except Exception as e:
        logging.error(f"Error: {e}")
        print("An error occurred. Check log.txt")

# ----------------------------
# Run Program
# ----------------------------
if __name__ == "__main__":
    source = input("Enter the file or folder path to add: ").strip('"')
    # Automatically detect project path (script folder)
    project = os.path.dirname(os.path.abspath(__file__))
    organize_files(source, project)