from math import ceil

print(50+50)
# 100

print(100-10)
# 90

#print(30+*6)
# Traceback (most recent call last):
#   File "Python1-2.py", line 1, in <module>
#     print(30+*6)
# TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

print(6^6)
# 0

print(6**6)
# 729

print(6+6+6+6+6+6)
# 36




p = int(input("Principal amount: "))
r = int(input("Interest rate: "))/100
l = int(input("Length in months: "))

m = ceil((p*((r/12)*((1+(r/12))**l)))/(((1+(r/12))**l)-1))

print(m)
