from pathlib import Path

#Absolute path - from the route f our hard disk:\Users\hp\PycharmProjects\Learning python

#Relative path

path = Path("ecommerce")
print(path.exists())

#path=Path("emails")
#print(path.mkdir())  #make directory

#path = Path("emails")
#print(path.rmdir())  #remove directory

path = Path ()
for file in path.glob("*.py"):
    print(file)

path = Path ()
for file in path.glob("*"):
    print(file)