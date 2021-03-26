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

payload = {'inUserName': 'kiemsi20@yahoo.com', 'inUserPass': 'miyukinogizaka06071997'}
url = 'https://www.facebook.com/'

def approach_with_request():
    with requests.Session() as s:
        r = s.post(url, data=payload)
        # r = s.get('A protected web page url')

    with open("test_html/index.html", "w", encoding="utf-8") as f:
        f.write(r.text)
# jazoest: 2921
# lsd: AVpk4aeNCl0
# email: kiemsi20@yahoo.com
# login_source: comet_headerless_login
# next:
# encpass: #PWD_BROWSER:5:1616675142:AdZQAOnLvZ5LRvvKsLmeyaEKmm2jiMhWM/RG0RojNB4JAYAEvHwq2/H/CYqAaXiVg0A9xB5dBOLRri717IKQulAAORKkqCapJYj3p0WypcJ1mPK1AYeSBb4x58eUdobVUSWCVwcVoc01oTXjsFhZbEmoVZhLXYtrs7Q=
# jazoest: 2962
# lsd: AVpk4aeNELw
# email: kiemsi20@yahoo.com
# login_source: comet_headerless_login
# next:
# encpass: #PWD_BROWSER:5:1616676462:AdZQAFb6H4OcJ/r9/eG2RPtLZErfx9GcbdD6mfwO6tw3O2EDPs134astHSITkt4gioXtClHe8LjsNSxE8ZsCj5+KxkALobyugwY5Uq1/CxGQZnohiyoTFd0iGgGWzfqK9ndq2gWbZXcfWsPT+k5OnxtYtwZ9AmJI/4A=

import mechanize

def approach_with_mechanize():

    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent',
                           'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)

    url = 'http://www.facebook.com/login.php'
    browser.open(url)
    browser.select_form(nr=0)  # This is login-password form -> nr = number = 0
    browser.form['email'] = "kiemsi20@yahoo.com"
    browser.form['pass'] = "miyukinogizaka06071997"
    response = browser.submit()

    with open("test_html/index.html", "w", encoding="utf-8") as f:
        f.write(response.read().decode("utf-8"))



if __name__ == "__main__":
    approach_with_mechanize()
    # print(response.text)
