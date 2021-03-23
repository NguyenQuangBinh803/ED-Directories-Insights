import os
from HTMLGenerator import HTMLGenerator


def approach_1():
    html_generator = HTMLGenerator("test_html/05_test_html.html")

    with open("clone/direct.txt", "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    parent_path = "C:/Users/ASUS"

    array_of_original = []
    for _ in range(10):
        array_of_original.append('')
    layer_range = 0
    delimitter = "───"
    for line in lines[1:]:
        # print(len(line.split(delimitter)[0]), line.split(delimitter))
        if len(line.split(delimitter)[0]) <= 2:
            layer_range = 1
            array_of_original[layer_range] = line.split(delimitter)[-1][:-1]
            print('/'.join(array_of_original[:layer_range + 1]))
            html_generator.insert_path(line.split(delimitter)[0] + delimitter,
                                       parent_path + '/'.join(array_of_original[:layer_range + 1]),
                                       line.split(delimitter)[-1][:-1])
        if len(line.split(delimitter)[0]) in range(3, 6):
            layer_range = 2
            array_of_original[layer_range] = line.split(delimitter)[-1][:-1]
            print('/'.join(array_of_original[:layer_range + 1]))
            html_generator.insert_path(line.split(delimitter)[0] + delimitter,
                                       parent_path + '/'.join(array_of_original[:layer_range + 1]),
                                       line.split(delimitter)[-1][:-1])
        if len(line.split(delimitter)[0]) in range(7, 10):
            layer_range = 3
            array_of_original[layer_range] = line.split(delimitter)[-1][:-1]
            print('/'.join(array_of_original[:layer_range + 1]))
            html_generator.insert_path(line.split(delimitter)[0] + delimitter,
                                       parent_path + '/'.join(array_of_original[:layer_range + 1]),
                                       line.split(delimitter)[-1][:-1])
        if len(line.split(delimitter)[0]) in range(11, 14):
            layer_range = 4
            array_of_original[layer_range] = line.split(delimitter)[-1][:-1]
            print('/'.join(array_of_original[:layer_range + 1]))
            html_generator.insert_path(line.split(delimitter)[0] + delimitter,
                                       parent_path + '/'.join(array_of_original[:layer_range + 1]),
                                       line.split(delimitter)[-1][:-1])
        if len(line.split(delimitter)[0]) in range(15, 18):
            layer_range = 5
            array_of_original[layer_range] = line.split(delimitter)[-1][:-1]
            print('/'.join(array_of_original[:layer_range + 1]))
            html_generator.insert_path(line.split(delimitter)[0] + delimitter,
                                       parent_path + '/'.join(array_of_original[:layer_range + 1]),
                                       line.split(delimitter)[-1][:-1])


def approach_2(directory_path):
    html_generator = HTMLGenerator("test_html/04_test_html_n50.html")
    prev_list = []
    for _ in range(5):
        prev_list.append(' ')
    parent_path = ""
    prefix = "    "
    for current_directory, sub_directory, files in os.walk(directory_path, topdown=False):
        print(current_directory)
        for sub in sub_directory:
            list_of_layer = os.path.join(current_directory, sub).replace("\\", "/").split("/")
            for i in range(len(list_of_layer)):
                if i < len(prev_list):
                    if prev_list[i] != list_of_layer[i]:
                        html_generator.insert_path(prefix * i,
                                                   parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                         "//g00sv1"),
                                                   list_of_layer[i])
                else:
                    html_generator.insert_path(prefix * i,
                                               parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                     "//g00sv1"),
                                               list_of_layer[i])

            prev_list = list_of_layer
        for sub in files:
            list_of_layer = os.path.join(current_directory, sub).replace("\\", "/").split("/")
            for i in range(len(list_of_layer)):
                if i < len(prev_list):
                    if prev_list[i] != list_of_layer[i]:
                        html_generator.insert_path(prefix * i,
                                                   parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                         "//g00sv1"),
                                                   list_of_layer[i])
                else:
                    html_generator.insert_path(prefix * i,
                                               parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                     "//g00sv1"),
                                               list_of_layer[i])
            prev_list = list_of_layer
    print("Done")


def directory_to_html_style(directory_path, output_path):
    html_generator = HTMLGenerator(output_path)
    prev_list = []
    for _ in range(5):
        prev_list.append(' ')
    parent_path = ""
    prefix = "    "
    for current_directory, sub_directory, files in os.walk(directory_path, topdown=False):
        print(current_directory)
        for sub in sub_directory:
            list_of_layer = os.path.join(current_directory, sub).replace("\\", "/").split("/")
            path_level = "layer-"+str(len(list_of_layer))
            for i in range(len(list_of_layer)):
                if i < len(prev_list):
                    if prev_list[i] != list_of_layer[i]:
                        html_generator.insert_path_with_layer(prefix * i,
                                                   parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                         "//g00sv1"),
                                                   list_of_layer[i], path_level)
                else:
                    html_generator.insert_path_with_layer(prefix * i,
                                               parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                     "//g00sv1"),
                                               list_of_layer[i],path_level)

            prev_list = list_of_layer
        for sub in files:
            list_of_layer = os.path.join(current_directory, sub).replace("\\", "/").split("/")
            path_level = "layer-" + str(len(list_of_layer))
            for i in range(len(list_of_layer)):
                if i < len(prev_list):
                    if prev_list[i] != list_of_layer[i]:
                        html_generator.insert_path_with_layer(prefix * i,
                                                   parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                         "//g00sv1"),
                                                   list_of_layer[i], path_level)
                else:
                    html_generator.insert_path_with_layer(prefix * i,
                                               parent_path + "/".join(list_of_layer[:i + 1]).replace("clone",
                                                                                                     "//g00sv1"),
                                               list_of_layer[i], path_level)
            prev_list = list_of_layer
    print("Done")

if __name__ == "__main__":
    directory_path = "C:/Users/ASUS/Desktop/2021 Documents"
    output_path = "test_html/04_test_html_document.html"
    directory_to_html_style(directory_path, output_path)
