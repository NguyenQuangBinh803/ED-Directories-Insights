import os

if __name__ == "__main__":
    directory_path = "C:/Users/ASUS/Documents"
    for current_directory, sub_directory, files in os.walk(directory_path):
        for sub in sub_directory:

            copy_path = os.path.join(current_directory, sub).replace("\\", "/").replace("C:/Users/ASUS", "clone")
            print(copy_path)
            if not os.path.exists(copy_path):
                os.makedirs(copy_path)
        for sub in files:
            copy_path = os.path.join(current_directory, sub).replace("\\", "/").replace("C:/Users/ASUS", "clone")
            print(copy_path)
            if not os.path.exists(copy_path):
                os.makedirs(copy_path)

    print("Done")