from io import BytesIO
from io import StringIO
f = StringIO()
f.write('hello')
# 5
f.write(' ')
# 1
f.write('world!')
# 6
print(f.getvalue())
# hello world!


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# Hello!
# Hi!
# Goodbye!


f = BytesIO()
f.write('中文'.encode('utf-8'))
# 6
print(f.getvalue())
# b'\xe4\xb8\xad\xe6\x96\x87'
print('')
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
# b'\xe4\xb8\xad\xe6\x96\x87'
