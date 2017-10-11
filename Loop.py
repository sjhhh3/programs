"""
# for
foods=['bacon','ham','burger','beef']
print(foods)
for f in foods[1:]:
    print(f,end=" ")
    print(len(f),end=" ")


# start, end, increment
for x in range(2,10,2):
    print(x,end=" ")

# while
start = 1
while start<10:
    print(start)
    start+=2

# break
number = 26
for n in range(0,101,2):
    if n is number:
        print(n,'is the answer')
        break
    else:
        print(n)

#homework1
start = 1
while start<1000:
    print(start)
    start*=2

#homework2
for n in range(1,100):
    if n%4==0:
        print(n)
    n+=1

# Continue, skip the loop this time
numbers=[2,35,52,17,26]
print("Here're the numbers still available")
for n in range(1,55):
    if n in numbers:
        continue
    print(n)
"""

