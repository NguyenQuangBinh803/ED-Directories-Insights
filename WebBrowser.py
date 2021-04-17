import requests
import eventlet
eventlet.monkey_patch()
from WebBrowserConstant import *
from WebDataExtractor import WebDataExtractor

class WebBrowser:
    def __init__(self, original_file, output_file):
        self.list_of_original_folder = open(original_file, "r", encoding="utf-8").readlines()
        self.web_data_extractor = WebDataExtractor()
        self.export_file = open(output_file, "w", encoding="utf-8")
        self.layer = []
        for _ in range(10):
            self.layer.append("")
        self.layer_count = 1


    def handle_login(self, session):
        try:
            with eventlet.Timeout(10):
                response = session.post(HOME_PAGE, headers=LOGIN_REQUEST_HEADER, data=LOGIN_PAY_LOAD)
                return response.status_code
        except Exception as exp:
                print("Login Exception ", str(exp))

    def handle_file_index(self, session, original_folder_link):
        with eventlet.Timeout(10):
            response = session.get(original_folder_link)
            print("File Index Request Done!")
            return response.content.decode('cp932', errors='ignore')
            # with open("test_html/01_test_link_acquistion_fileindex.html", "w") as file:
            #     file.write(response.content.decode('cp932', errors='ignore'))

    def handle_session(self):
        with requests.session() as session:
            self.handle_login(session)
            for original_folder in self.list_of_original_folder:
                folder_name, folder_link_id = original_folder.split('-')[0], original_folder.split('-')[1][:-1]
                folder_link = FILE_INDEX_PAGE + folder_link_id
                self.browse(session, folder_name, folder_link, 1)

    def browse(self, session, folder_name, folder_link, layer_count):
        self.layer[layer_count] = folder_name
        self.export_file.write("/".join(self.layer[:layer_count]) + EOF)
        print("/".join(self.layer[:layer_count]) + EOF)
        response_content = self.handle_file_index(session, folder_link)
        self.web_data_extractor.insert_html_document(response_content)
        folder_empty, folder_list = self.web_data_extractor.extract_folder()
        file_empty, file_list = self.web_data_extractor.extract_file()
        if not file_empty:
            for file in file_list:
                self.export_file.write("/".join(self.layer[:layer_count]) + "/" + file["name"] + EOF)
                print("/".join(self.layer[:layer_count]) + "/" + file + EOF)
        if folder_empty:
            return
        else:
            for folder in folder_list:
                self.browse(session, folder["name"], folder["address"], layer_count + 1)

if __name__ == "__main__":
    browser = WebBrowser("test_html/01_test_list_of_original_folder.txt", "test_html/cybozu_directory.txt")
    # print(browser.list_of_original_folder)
    browser.handle_session()
