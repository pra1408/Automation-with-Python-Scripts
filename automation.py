import os
import shutil

# Define the source directory where files are to be organized
source_dir = 'C://Users//User//Desktop//code//task4//New folder'  # Change this to your directory path

# Define the directory mapping based on file extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
}

def organize_files():
    for filename in os.listdir(source_dir):
        # Skip directories
        if os.path.isdir(os.path.join(source_dir, filename)):
            continue

        # Determine the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Find the appropriate folder for the file
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                destination_dir = os.path.join(source_dir, folder)
                break
        else:
            # If no matching folder is found, use "Others" folder
            destination_dir = os.path.join(source_dir, 'Others')

        # Create the folder if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Move the file to the appropriate folder
        shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

        print(f"Moved: {filename} -> {destination_dir}")

if __name__ == '__main__':
    organize_files()
