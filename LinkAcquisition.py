import requests




inside_folder_division = "class=\"marginHalf\""
# All folder links are stored in table inside this division

inside_file_division = "class=\"filemanage-nofiles-title\""
# If this class name is found then there is no files inside

SIGN_FOLDER_EMPTY = "サブフォルダなし"
SIGN_FILE_EMPTY = "ファイルがありません。"

file_not_empty = "id=\"js-filemanage-view-area\""
# This is division id
# data inside <tr class=js-scroll-pos listview-item-row   ----> Loop all same class name for query
if __name__ == "__main__":
    pass