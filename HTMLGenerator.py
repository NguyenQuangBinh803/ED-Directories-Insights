import os


class HTMLGenerator:
    def __init__(self, file_name):
        self.html_file = open(file_name, "w", encoding="utf-16")
        self.html_file.write("<html>\n")

    def insert_path(self, prefix, path_address, path_basename):
        self.html_file.write("<pre>")
        self.html_file.write(prefix)
        self.html_file.write("<a href=\"" + path_address + "\">")
        self.html_file.write(path_basename)
        self.html_file.write("</a>")
        self.html_file.write("</pre>\n")


if __name__ == "__main__":
    html_generator = HTMLGenerator("test_html/01_test_html.html")
    html_generator.insert_path("    │   ├───",
                               "C:/Users/ASUS/Desktop/2021-Projects/Python-Projects/ED-Directories-Insights/clone",
                               "bandicam 2020-11-12 21-03-29-773.mp4")
    html_generator.insert_path("    │   ├───",
                               "C:/Users/ASUS/Desktop/2021-Projects/Python-Projects/ED-Directories-Insights/clone",
                               "bandicam 2020-11-12 21-03-29-773.mp4")
    html_generator.insert_path("    │   ├───",
                               "C:/Users/ASUS/Desktop/2021-Projects/Python-Projects/ED-Directories-Insights/clone",
                               "bandicam 2020-11-12 21-03-29-773.mp4")
    html_generator.insert_path("    │   ├───",
                               "C:/Users/ASUS/Desktop/2021-Projects/Python-Projects/ED-Directories-Insights/clone",
                               "bandicam 2020-11-12 21-03-29-773.mp4")