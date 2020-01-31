f = "C:/WebInfo/t66y.csv"

lines = open(f, 'r').readlines()
start = 1200

end = start + 50
if end > len(lines):
    end = len(lines)
for n, line in enumerate(lines[start:end]):
    print(n, " : ", line, end="")
