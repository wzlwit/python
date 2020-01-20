import io
import sys
import time
import requests
from html.parser import HTMLParser


def main():
    parser = HTMLParser()
    fTemp = "C:/WebInfo/temp.html"
    root = 'https://www.t66y.com'
    loop = 1

    for i in range(loop):
        num = i+1
        url = "{}/thread0806.php?fid=5&search=&page={}".format(root, num)
        # print(url)

        r = requests.get(url)
        ctn = r.content.decode('gbk')
        # print (ctn)

        # open(fTemp, 'w', encoding="utf-8").write(ctn)


if __name__ == "__main__":
    main()
