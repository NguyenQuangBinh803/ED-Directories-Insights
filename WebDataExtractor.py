'''
Author - Edward J. C. Ashenbert
Date - 26/3/2021
Description this file is built for prompt extraction of their web folders and files
'''

from bs4 import BeautifulSoup

PARAMETER_LINK_LENGTH_THRESHOLD = 100

class WebDataExtractor:
    def __init__(self):
        self.search_engine = None
        self.folder_division = None
        self.file_division = None

    def insert_html_document(self, response_document):
        self.search_engine = BeautifulSoup(response_document, features="html.parser")
        margin_half = self.search_engine.find_all(class_="marginHalf")
        self.folder_division = margin_half[0]
        self.file_division = margin_half[1]

    def extract_folder(self):
        folder_empty = False
        list_of_folder = []
        temporary = dict.fromkeys("name", "address")
        for link in self.folder_division.find_all("a"):
            temporary["name"] = link.text
            temporary["address"] = link["href"]
            list_of_folder.append(temporary)
            # print(link.text, link["href"])

        if len(list_of_folder) == 0:
            folder_empty = True
        return folder_empty, list_of_folder

    def extract_file(self):
        file_empty = False
        list_of_files = []
        temporary = dict.fromkeys("name", "address")
        for link in self.file_division.find_all("a"):
            if link.text is not None and len(link["href"]) > PARAMETER_LINK_LENGTH_THRESHOLD:
                temporary["name"] = link.text
                temporary["address"] = link["href"]
                list_of_files.append(temporary)
        if len(list_of_files) == 0:
            file_empty = True
        return file_empty, list_of_files


if __name__ == "__main__":
    file_name = "C:/Users/binh_nguyen/Documents/ADTEC-Document Sites/folder_example_01.html"
    # html_scraper = HTMLScraper("C:/Users/binh_nguyen/Documents/ADTEC-Document Sites/folder_example_01.html")
    file = open(file_name, "r", encoding="utf-8").read()
    search_engine = BeautifulSoup(file, features="html.parser")
    margin_half = search_engine.find_all(class_="marginHalf")
    folder_division = margin_half[0]
    file_division = margin_half[1]
    print("Folder Links")
    for link in folder_division.find_all("a"):
        print(link.text, link["href"])

    print("File Links")
    for link in file_division.find_all("a"):
        if link.text is not None and len(link["href"]) > PARAMETER_LINK_LENGTH_THRESHOLD:
            print(link.text, link["href"])
