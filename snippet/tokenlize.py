import json
import pickle
d = dict(name='Bob', age=20, score=88)
print(d)

out = pickle.dumps(d)
print(out)
# b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


""" 
JSON类型	Python类型
{}	        dict
[]	        list
"string"	str
1234.56	    int或float
true/false	True/False
null	    None
"""
print('\nJASON:')
d = dict(name='Bob', age=20, score=88)
out = json.dumps(d)
print(out)
# '{"age": 20, "score": 88, "name": "Bob"}

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(f'\njson_str: {json_str}')
out = json.loads(json_str)
print(out)
# {'age': 20, 'score': 88, 'name': 'Bob'}
