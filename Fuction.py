'''
# Function
def food():
    print("this is a function")

def bitcoin_to_usd(btc):
    usd = 2623.123 * btc
    print('$',usd)
bitcoin_to_usd(2.123)


# Return Value
def dating_age(myage):
    #for girlsage in range(myage-3,myage+3):
        #print(girlsage)
    girlsage = myage/2+7
    return girlsage
print (dating_age(23))



# Default Argument
def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'

    print(sex)
get_gender()


def keyword(name='jason',action='eat',item='burger'):
    print(name,action,item)
keyword()
keyword('key','did','nothing')
'''

def hc(age, apple, smoke,*arg):
    print(age,apple,smoke,*arg)
mydata=[23,3,5,1]
hc(mydata[0],mydata[1],mydata[2])
hc(*mydata)