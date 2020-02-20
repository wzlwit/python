from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # * value starts from 1

# Print Output:
# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12


@unique  # * DECORATOR: keep unique / no duplicates
class Weekday(Enum):
    # Key-Value pair, static class
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
# Weekday.Mon
print(Weekday.Tue)
# Weekday.Tue
print(Weekday['Tue'])
# Weekday.Tue
print(Weekday.Tue.value)
# 2
print(day1 == Weekday.Mon)
# True
print(day1 == Weekday.Tue)
# False
print(Weekday(1))
# Weekday.Mon
print(day1 == Weekday(1))
# True
Weekday(7)
# Traceback (most recent call last):
#   ...
# ValueError: 7 is not a valid Weekday
for name, member in Weekday.__members__.items():
    print(name, '=>', member)
