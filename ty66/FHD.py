import io
import sys
import time
import requests
from html.parser import HTMLParser


def main():
    parser = HTMLParser()
    fTemp = "C:/WebInfo/temp.html"
    root = 'https://www.t66y.com/'
    loop = 0

    for i in range(loop):


    url = 'https://www.t66y.com/thread0806.php?fid=5'
    r = requests.get(url)
    ctn = r.content.decode('gbk')
    print (ctn)

    # open(fTemp, 'w', encoding="utf-8").write(ctn)


if __name__ == "__main__":
    main()
