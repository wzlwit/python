# separate words from chinese

word = jieba.cut("一句中文")
print(".".join(word))