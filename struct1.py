'''
from _struct import *

# Store as bytes data
str = pack('iif', 1, 2, 5.324)

ori = unpack('iif',b'\x01\x00\x00\x00\x02\x00\x00\x005^\xaa@')
print(ori)


income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)
'''

a=2
b=1
print(a!=b)
print(a&b)
print(a|b)