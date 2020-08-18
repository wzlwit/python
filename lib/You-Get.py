# video download
you-get 'url'

# ex1
mlurl = ['https://www.bilibili.com/video/av10590361/#page={p}'.format(p=p) for p in range(1,40)]
mlpath = 'I:/machine_learning/lihongyi_ml'
for url in mlurl:
    os.system("you-get -o {path} {url} ".format(path=mlpath,url=url))
print('all done!')