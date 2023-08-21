import os
import shutil

def copy_and_rename_files(src_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)

            # Specify the filename pattern to be copied
            if "a_b_blue.txt" in file:
                dest_path = os.path.join(root, file)

                file_name, file_extension = os.path.splitext(file)
                dest_filename = f"{file_name}_blue{file_extension}"

                dest_file_path = os.path.join(root, dest_filename)

                while os.path.exists(dest_file_path):
                    dest_filename = f"{file_name}_blue{file_extension}"
                    dest_file_path = os.path.join(root, dest_filename)

                shutil.copy(src_path, dest_file_path)
                print(f"Copied {src_path} to {dest_file_path}")

if __name__ == "__main__":
    source_directory = "/home/hardikmb/codebase/scripts/Python"  # Replace with the actual source directory

    copy_and_rename_files(source_directory)
