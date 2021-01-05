from urllib import error
import requests
import os


class Web_url_test():
    def __init__(self):
        self.menu = []
        self.errorurl = []

    def get_menu(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split()
                print(line)
                self.menu.append(line)

    def web_is_working(self, main, num):
        urls = []
        for i in range(1, num+1):
            url_web = "https://projector-specification-documents.readthedocs.io/en/latest/" + main + ".html#id" + str(i)
            urls.append(url_web)
        for url in urls:
            try:
                requests.get(url, verify=False)
                print(url, "OK")
            except error.URLError as e:
                print(url, "Not Working")
                self.errorurl.append(url)



if __name__ == '__main__':
    web_url_test = Web_url_test()
    web_url_test.get_menu(".\menu.txt")
    for item in web_url_test.menu:
        web_url_test.web_is_working(item[0], int(item[1]))