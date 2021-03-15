import os
from HTMLGenerator import HTMLGenerator

if __name__ == "__main__":
    html_generator = HTMLGenerator("test_html/02_test_html.html")
    with open("clone/direct.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        # print(lines)
    array_of_original = []
    for _ in range(10):
        array_of_original.append('')

    orginal_count = 0
    for line in lines:
        if "└───" in line:
            array_of_original[orginal_count] = line.split("└───")[1]
            orginal_count += 1
        # print(array_of_original)
        print(line[:-1])
