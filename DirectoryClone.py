from contextlib import contextmanager
import os
import sys


def approach_2(directory_path):

    container_path = os.path.normpath(
        directory_path + os.path.sep + os.path.pardir).replace("\\", "/")
    browsing_count = 0
    parent_path = "C:/Users/binh_nguyen/clone/"
    os.chdir(parent_path)
    prev_path = ''
    for current_directory, sub_directory, files in os.walk(directory_path):
        copy_path = current_directory.replace(
            "\\", "/").replace(container_path, "clone_3/")
        print(copy_path, prev_path)
        browsing_count += 1
        print("Done Browsing " + str(browsing_count) + " Round", copy_path)

        try:
            if prev_path == '' or prev_path == copy_path:
                if not os.path.exists(copy_path):
                    os.makedirs(copy_path)

            else:
                while prev_path in copy_path:
                    os.chdir("..")

            prev_path = current_directory
        except Exception as exp:
            print("Error in changin direcory")
            print(str(exp))
            print(copy_path)
            sys.exit()

        for sub in sub_directory:
            try:
                if not os.path.exists(sub):
                    os.makedirs(sub)
            except Exception as exp:
                print(str(exp))
                print((os.path.join(copy_path, sub)))
                sys.exit()

        for sub in files:
            try:
                if not os.path.exists(sub):
                    os.makedirs(sub)
            except Exception as exp:
                print(str(exp))
                print((os.path.join(copy_path, sub)))
                sys.exit()
            # os.makedirs(files)


def approach_1():
    directory_path = "//g00sv1/N50/G51/"
    for current_directory, sub_directory, files in os.walk(directory_path):
        for sub in sub_directory:
            copy_path = os.path.join(current_directory, sub).replace(
                "\\", "/").replace("//g00sv1/N50/", "clone")
            # print(copy_path)
            try:
                if not os.path.exists(copy_path):
                    os.makedirs(copy_path)
            except FileNotFoundError:
                print(copy_path)
                sys.exit()
        for sub in files:
            copy_path = os.path.join(current_directory, sub).replace(
                "\\", "/").replace("//g00sv1/N50/", "clone")
            # print(copy_path)
            try:
                if not os.path.exists(copy_path):
                    os.makedirs(copy_path)
            except FileNotFoundError:
                print(copy_path)
                sys.exit()
    print("Done")


if __name__ == "__main__":
    clone_directory = "C:/Users/ASUS/Documents"
    os.chdir(clone_directory)
    # os.makedirs("e7bfc592dd58160a673354133ca845a6de0c51")
    
    directory_path = "C:/Users/ASUS/Desktop"
    container_path = os.path.normpath(
        directory_path + os.path.sep + os.path.pardir).replace("\\", "/")
    prev_path = ''
    for current_directory, sub_directory, files in os.walk(directory_path):
        
        # copy_path = clone
        copy_path = current_directory.replace(
            "\\", "/").replace(container_path, "clone_desktop")
        
        if prev_path == '' or len(prev_path.split("/")) <= len(copy_path.split("/")):
            if not os.path.exists(copy_path.split('/')[-1]):
                os.makedirs(copy_path.split('/')[-1])
            os.chdir(copy_path.split('/')[-1] + "/")
            print(os.getcwd())
            print("="*100)
            print("Need to Change Directory")
            print("Previous Path ", prev_path)
            print("Current Path ", copy_path)
            prev_path = copy_path
            for sub in sub_directory:
                if not os.path.exists(sub):
                    os.makedirs(sub)
            
            for sub in files:
                if not os.path.exists(sub):
                    os.makedirs(sub)
            

        elif len(prev_path.split("/")) > len(copy_path.split("/")):
            print("="*100)
            print("Need to Change Directory")
            print("Previous Path ", prev_path)
            print("Current Path ", copy_path)
            while len(prev_path.split("/")) >= len(copy_path.split("/")):
                prev_path = os.path.normpath(
                    prev_path + os.path.sep + os.path.pardir).replace(
                    "\\", "/")
                os.chdir("..")

            print("After Change", prev_path)
            print(os.getcwd())
            if not os.path.exists(copy_path.split('/')[-1]):
                os.makedirs(copy_path.split('/')[-1])
            os.chdir(copy_path.split('/')[-1])
            print(os.getcwd())
            for sub in sub_directory:
                if not os.path.exists(sub):
                    os.makedirs(sub)
            
            for sub in files:
                if not os.path.exists(sub):
                    os.makedirs(sub)
            
            prev_path = copy_path
            print("="*100)
