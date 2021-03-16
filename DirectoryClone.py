import os

if __name__ == "__main__":
    directory_path = "//g00sv1/N10"
    for current_directory, sub_directory, files in os.walk(directory_path):
        for sub in sub_directory:
            copy_path = os.path.join(current_directory, sub).replace("\\", "/").replace("//g00sv1", "clone")
            # print(copy_path)
            try:
                if not os.path.exists(copy_path):
                    os.makedirs(copy_path)
            except FileNotFoundError:
                print(copy_path)
        for sub in files:
            copy_path = os.path.join(current_directory, sub).replace("\\", "/").replace("//g00sv1", "clone")
            # print(copy_path)
            try:
                if not os.path.exists(copy_path):
                    os.makedirs(copy_path)
            except FileNotFoundError:
                print(copy_path)
    print("Done")