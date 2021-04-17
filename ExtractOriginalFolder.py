from bs4 import BeautifulSoup as bs

if __name__ == "__main__":
    with open("C:/Users/binh_nguyen/Documents/ADTEC-Document Sites/file_index.log", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("test_html/01_test_list_of_original_folder.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write('-'.join([line.split("\"")[1], line.split("\"")[5]]) + "\n")
    print("Done extracting origins")
