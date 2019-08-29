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
    fName = "C:/Dev/WebInfo/temp.txt"
    url = 'https://www.rona.ca/en'
    r = requests.get(url)
    ctn = r.content.decode('utf-8')
    print (ctn)

    open(fName, 'w', encoding="utf-8").write(ctn)


if __name__ == "__main__":
    main()
