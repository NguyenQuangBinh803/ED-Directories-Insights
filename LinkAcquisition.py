from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup as bs
import re
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
    response = requests.get("http://cybozu.adtec-eng.co.jp/cb7/ag.exe?page=FileIndex",
                            auth=HTTPDigestAuth('binh_nguyen', 'adtub684'))
    print(response.content.decode("utf-8"))

# csrf_ticket:
# _System: login
# _Login: 1
# LoginMethod: 2
# _Account: binh_nguyen
# Password: adtub684
# Submit: ログイン
