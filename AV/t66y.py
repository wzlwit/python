# from html.parser import HTMLParser
import io
import sys
import requests
import re
import time
from datetime import date

fTemp = "C:/WebInfo/temp.html"
f = "C:/WebInfo/t66y.csv"
root = 'https://www.t66y.com'
# date =date.today().strftime("%y-%m-%d")
# date = date.today().isoformat()


def animation():
    up = 1
    # for i in range(up,up+325):
    for i in range(up, up+2):
        num = i
        url = "{}/thread0806.php?fid=5&search=&page={}".format(root, num)
        print(url)
        r = requests.get(url)
        ctn = r.content.decode('gbk')
        # ctn = r.content.decode('gbk').encode('utf-8').decode('utf-8')
        # open(fTemp, 'w', encoding='gbk').write(ctn)

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
            suffix = re.search("[./]?无码.*MP4[./]?[0-9MGB.]*", h3)
            if suffix:
                suffix = suffix.group(0)
                # print(suffix)
                title = h3[66:-9].replace('「', '').replace('」', "").split(
                    ")")[-1].split("]")[-1].replace(suffix, '').strip()

                size = suffix.split("/")[-1]
                mPos = size.find('M')
                if mPos > 0:
                    size = "{0:.3f}GB".format(int(size[:mPos-1])/1024)

                titleL = open(f, 'r').read()

                if not title in titleL:
                    hrefE = h3.split('"')[1]
                    href = "{}/{}".format(root, hrefE)
                    date = dates[n].split(">")[1].strip()
                    strAdd = '"{}",{},=hyperlink("{}"),{},动画'.format(
                        title, size, href, date)
                    print(strAdd)
                    open(f, 'a', encoding="gbk").write('{}\n'.format(strAdd))

        time.sleep(2)


def main():
    animation()
    print('Exit')


if __name__ == "__main__":
    main()
