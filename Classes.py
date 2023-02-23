class Robot:
    def __init__(self,name,colour, age):
        self.name= name
        self.colour = colour
        self.age = age
    def introduce_self (self):
        message = (f"""My name is {self.name}
My favourite colour is {self.colour}
I am {self.age}""")
        return message


#The hashtagged code becomes useless after I introduce the concept on inheritances
#r1 = Robot()
#r1.name = "John"
#r1.colour = "blue"
#r1.age = 30
#print(r1.introduce_self())

#r2 = Robot()
#r2.name = "Mary"
#r2.colour = "red"
#r2.age = 42
#print(r2.introduce_self())

r3 = Robot(name="Stacy", colour="sage green", age=20)
print(r3.introduce_self())

####
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        print("draw")
    def move(self):
        print("move")


point1 = Point(10,8)
print(f"the coordinates are ({point1.x}, {point1.y})")
point1.draw()

point2 = Point(6,7)
point2.x = 14
print(point2.x)

#####
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi my name is {self.name}")


one = Person("Bill")
one.talk()

two = Person("Bobby")
two.talk()


###
#Inheritances
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass    #avoid error

dog1= Dog()
dog1.walk()
dog1.bark()


