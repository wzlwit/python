""" 
py C:/Users/zhaolongw/Desktop/repos/python/web/WebRequest.py
"""

import io
import sys
import time
from urllib.request import urlopen, Request

def main():
    # reload(sys)
    # sys.setdefaultencoding('UTF8')
    fName = "C:/Dev/WebInfo/temp.html"
    url = 'https://www.rona.ca/en'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    req = Request(url=url, headers=headers) 
    ctn = urlopen(req).read().decode()
    # print (ctn)

    open(fName, 'w', encoding="utf-8").write(ctn)


if __name__ == "__main__":
    main()
