course = 'Python course for beginners'
print(course)
print(course[0])
print(course[-1])
print(course[0:6])  #python index starts from zero, last index is -1 [0:6} returns characters from index 0 to index 5 exluding index 6
print(course[1: ])
another= course[:]  #cloning
print(another)
course1 = "Python's course for beginners"
print(course1)

#Long strings eg messages sent in email
course3 = '''
Hey Lynn ,
This is our first email to you
Regards
Stacy'''
print(course3)

name = "Jeniffer"
print(name[1:-1])

#Strings formatting
firstname =" Lynn"
secondname ="Stacy"

message = firstname + " [" + secondname + "] " + "is a coder"
#formatted string
msg = f'{firstname}[{secondname}] is a coder'
print(msg)
print(message)

#String methods
print(len(course))
print(course.upper())
print(course.lower())
print(course.find("n")) #find function is case sensitive and returns index of character
print(course.find("beginners"))
print(course.replace("beginners","absolute beginners"))
print("Python" in course) #in operator produces a Boolean Value; True or False