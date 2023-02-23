#ValueError ;  is an exception that occurs when a function receives an argument of the correct data type but an inappropriate value.
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid error")

try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income/age
except ZeroDivisionError:
    print("Age can not be zero")
except ValueError:
    print("Invalid error")