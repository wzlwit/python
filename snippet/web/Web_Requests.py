""" 
py C:/Users/zhaolongw/Desktop/repos/python/web/WebRequest.py
"""

import io
import sys
import time
import requests
from html.parser import HTMLParser


def main():
    parser = HTMLParser()
    fName = "C:/WebInfo/temp.html"
    # url = 'https://www.rona.ca/en'
    url = 'https://www.t66y.com/thread0806.php?fid=5'
    r = requests.get(url)
    # ctn = r.content.decode('utf-8')
    ctn = r.content.decode('gbk')
    # print (ctn)

    open(fName, 'w', encoding="utf-8").write(ctn)


if __name__ == "__main__":
    main()
