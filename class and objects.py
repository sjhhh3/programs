'''
class Enemy:
    life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def check(self):
        if self.life <= 0:
            print("you died")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy()
enemy2.life = 1
enemy1.attack()
enemy1.check()
enemy2.attack()
enemy2.check()


# init
class fish:
    def __init__(self,amount,name):
        self.number = amount
        self.classname = name

    def swim(self):
        print(str(self.number) + " " + str(self.classname) + " are swimming")

flipper = fish(6,'flippers')
flipper.swim()


# inheritance
class Parent():
    def print_last_name(self):
        print('Lavernz')

class Child(Parent):
    def name(self):
        print('Steve',end=' ')
        self.print_last_name()

man = Child()
man.name()
'''

# inheritance2
class boy():

    def printboy(self):
        print('he')

class girl():

    def printgirl(self):
        print('she')

class fuck(boy,girl):
    def printtwo(self):
        self.printboy()
        self.printgirl()

two = fuck()
two.printtwo()


