'''
# unpack
date,name,price = ['December 23, 2016', 'Jerry John', 9.32]
print(date)
print(name)
print(price)

def drop_first_last(grades):
    grades.sort()
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)
    print(middle)

drop_first_last([77,68,90,100,85,1])


# ZIP
first = ['Tom','Mary','Jerry']
last = ['Kern','Jane','Fox']

names = zip (first,last)
for a,b in names:
    print(a,b)

# Lambda
answer = lambda x: x*7
print(answer(5))
'''