from ExcelGenerator import ExcelGenerator
import os
import re


class DirectoryExplore:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def patse_directory(self, file_name):
        excel_generator = ExcelGenerator(file_name)
        browse_count = 0
        directory_count = 0
        for current_directory, sub_directory, files in os.walk(self.directory_path):
            # print(os.path.basename(current_directory), sub_directory, files)
            # print(current_directory)
            browse_count += 1
            print(current_directory)
            if browse_count != 1:
                for sub in sub_directory:
                    directory_count += 1
                    layer_list = os.path.join(
                    current_directory, sub).replace("\\", "/").split("/")
                
                    for index, layer in enumerate(layer_list):
                        excel_generator.insert_cell_value(
                            directory_count, index + 1, layer)
                        excel_generator.insert_cell_hyperlink(
                        directory_count, len(layer_list) - index, os.path.normpath(os.path.join(current_directory, sub) + (os.path.sep + os.path.pardir)*(index)))

            for file in files:
                directory_count += 1
                layer_list = os.path.join(
                    current_directory, file).replace("\\", "/").split("/")
                for index, layer in enumerate(layer_list):
                    excel_generator.insert_cell_value(
                        directory_count, index + 1, layer)
                    excel_generator.insert_cell_hyperlink(
                        directory_count, len(layer_list) - index, os.path.normpath(os.path.join(current_directory, file) + (os.path.sep + os.path.pardir)*(index)))

            # break
if __name__ == '__main__':
    directory_explore = DirectoryExplore("C:/Users/ASUS/Documents")
    directory_explore.patse_directory("test_excel/02_test_patse_result.xlsx")
    # layer_1 = ['A', 'B', "C"]
    # layer_2 = [['A',"D","D","D","D"], ["D","D","D","D"]]
    # layer_3 = [[['','R'], ['','R']], [['','R'], ['','R']]]
    # layer = []
    # layer.append(layer_1)
    # layer.append(layer_2)
    # layer.append(layer_3)

    # Base on the number of leyer we will take our collumn apparently
    # print(layer[2][0][1])
