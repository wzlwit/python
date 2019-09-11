# https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/11.%E6%96%87%E4%BB%B6%E5%92%8C%E5%BC%82%E5%B8%B8.md

""" 
JSON 	            Python
object 	            dict
array 	            list
string  	        str
number (int/real) 	int / float, int- & float-derived Enums
true / false 	    True / False
null 	            None
"""

import json

def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()



""" 
4个比较重要的函数，分别是：

    dump - 将Python对象按照JSON格式序列化到文件中
    dumps - 将Python对象处理成JSON格式的字符串
    load - 将文件中的JSON数据反序列化成对象
    loads - 将字符串的内容反序列化成Python对象


"""

dict()