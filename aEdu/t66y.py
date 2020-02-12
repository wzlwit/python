# from html.parser import HTMLParser
import io
import sys
import requests
import re
import time
from datetime import date
from urllib.request import urlopen, Request

fTemp = "C:/WebInfo/temp.html"
f = "C:/WebInfo/t66y.csv"
# f = "C:/WebInfo/t66y_test.csv"
root = 'https://www.t66y.com'

# date =date.today().strftime("%y-%m-%d")
# date = date.today().isoformat()


def animation():
    up = 1
    # for i in range(up,up+325):

    for i in range(up, up+3):
        num = i
        url = "{}/thread0806.php?fid=5&search=&page={}".format(root, num)
        print(url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        req = Request(url=url, headers=headers)
        ctn = urlopen(req).read().decode('gbk')

        # r = requests.get(url)
        # ctn = r.content.decode('gbk')
        # ctn = r.content.decode('gbk').encode('utf-8').decode('utf-8')

        # open(fTemp, 'w', encoding='gbk').write(ctn)
        # print(ctn)

        # date = re.search("[0-9]{4}[/-]?[0-9]{2}[/-]?[0-9]{2}",ctn)
        h3s = re.findall('<h3><a href="htm_data.*</h3>', ctn)

        # dates = re.findall('(?=<td><a href=\".*class=\"f10\">[ ])[0-9]{4}[/-]?[0-9]{2}[/-]?[0-9]{2}',ctn)
        dates = re.findall(
            'class="f10">\s[0-9]{4}[/-]?[0-9]{2}[/-]?[0-9]{2}', ctn)
        # (?<=[ ][0-9:]{5})

        if len(dates) > len(h3s):
            dDif = len(dates)-len(h3s)
            dates = dates[dDif:]

        # print(len(h3s))
        # print(len(dates))

        for n, h3 in enumerate(h3s):
            suffix = re.search("[./]?无码[./]*MP4[./]?[0-9MGB.]+", h3)
            if suffix:
                suffix = suffix.group(0)
                # print(suffix)
                title = h3[66:-9].replace('「', '').replace('」', "").split(")")[-1].split(
                    "]")[-1].replace(suffix, '').replace("[", "").strip()

                size = suffix.split("/")[-1]
                # mPos = size.find('M')
                # if mPos > 0:
                #     size = "{0:.3f}GB".format(int(size[:mPos])/1024)

                titleL = open(f, 'r').read()

                if not title in titleL:
                    hrefE = h3.split('"')[1]
                    href = "{}/{}".format(root, hrefE)
                    date = dates[n].split(">")[1].strip()
                    strAdd = '"{}",{},{},动画,=hyperlink("{}")'.format(
                        title, size, date, href)
                    print(strAdd)
                    open(f, 'a', encoding="gbk").write('{}\n'.format(strAdd))
        time.sleep(2)


def foreign():
    f = "C:/WebInfo/t66y_for.csv"

    up = 1
    for i in range(up, up+4):
        num = i
        url = "{}/thread0806.php?fid=4&search=&page={}".format(root, num)
        print(url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
        req = Request(url=url, headers=headers)
        ctn = urlopen(req).read().decode('gbk')

        # r = requests.get(url)
        # ctn = r.content.decode('gbk')
        # ctn = r.content.decode('gbk').encode('utf-8').decode('utf-8')

        # open(fTemp, 'w', encoding='gbk').write(ctn)

        h3s = re.findall('<h3><a href="htm_data.*</h3>', ctn)

        # dates = re.findall('(?=<td><a href=\".*class=\"f10\">[ ])[0-9]{4}[/-]?[0-9]{2}[/-]?[0-9]{2}',ctn)
        dates = re.findall(
            'class="f10">\s[0-9]{4}[/-]?[0-9]{2}[/-]?[0-9]{2}', ctn)
        # (?<=[ ][0-9:]{5})

        if len(dates) > len(h3s):
            dDif = len(dates)-len(h3s)
            dates = dates[dDif:]

        # print(len(h3s))
        # print(len(dates))

        for n, h3 in enumerate(h3s):
            # print(h3)
            prefix = re.search("FHD", h3)
            if prefix:
                prefix = prefix.group(0)
                # print(prefix)
                title = h3[66:-9].split("]")[1].replace(prefix, '').strip()
                size = ''
                # size = suffix.split("/")[-1]

                titleL = open(f, 'r').read()

                if not title in titleL:
                    hrefE = h3.split('"')[1]
                    href = "{}/{}".format(root, hrefE)
                    date = dates[n].split(">")[1].strip()
                    strAdd = '"{}",{},{},欧美,=hyperlink("{}")'.format(
                        title, size, date, href)
                    print(strAdd)
                    open(f, 'a', encoding="gbk").write('{}\n'.format(strAdd))
        time.sleep(2)


def main():
    animation()
    foreign()
    print('Exit')


if __name__ == "__main__":
    main()
