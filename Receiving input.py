
name= input("What is your name?  ")
colour = input("What is your favourite colour?  ")
print(name + " likes " + colour)

#Type conversion
birth_year = input("Birth year:  ")
age = 2023 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input("Weight in pounds:  ")
gender = input("Gender ")
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)
print( name + " is a " + str(age) + " year old " + gender.lower() +" who weighs "+ str(weight_kg) + " kilograms.")