import os


class HTMLGenerator:
    def __init__(self, file_name):
        self.html_file = open(file_name, "w", encoding="utf-16")
        self.html_file.write("<html>\n")
        self.div_count = 0

    def insert_path(self, prefix, path_address, path_basename):
        self.html_file.write("<pre>")
        self.html_file.write(prefix)
        self.html_file.write("<a href=\"" + path_address + "\">")
        self.html_file.write(path_basename)
        self.html_file.write("</a>")
        self.html_file.write("</pre>\n")

    def start_division(self, division_id, division_class):
        self.div_count += 1
        # What I'm thinking was how to really capture the text we need inside without manually starting ang closing
        self.html_file.write("<div ")

    def insert_path_with_layer(self, prefix, path_address, path_basename, path_level):
        self.html_file.write("<pre>")
        self.html_file.write(prefix)
        self.html_file.write("<a class=\"link_decorate\" href=\"" + path_address + "\">")

        self.html_file.write(path_basename)
        self.html_file.write("</a>")
        self.html_file.write(" <button class=\"collapsible\" ")
        self.html_file.write("id=\"btn-" + path_level + "\"")
        self.html_file.write("></button>")
        self.html_file.write("</pre>\n")

    def close_division(self):
        self.div_count -= 1
        self.html_file.write("</div>")


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
