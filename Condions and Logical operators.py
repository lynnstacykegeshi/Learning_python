is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

##
price = 1000000
good_credit = False

if good_credit:
    down_payment= int(0.1*price)
else:
    down_payment= int(0.2*price)
print(f"Downpayment is ${down_payment}")


####
#Logical operators; and , or, not
has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit and not has_criminal_record       :
    print("Participant is eligible for loan")
else:
    print("Not eligible for loan")

####
#Comparison operator; >,<,>=,<=, ==, !=
temp = 38
if temp == 30:
    print("It's a hot day")
else:
   print("It's not a hot day'")

name = "John"
print(len(name))
print(name.find("b"))
if len(name) < 3:
    print("Name should be at least 3 characters")
elif len(name) > 50:
    print("Name should not be more than 50 characters")
else:
    print("Proceed to the next prompt")

#####
weight = int(input("What is your weight:  "))
mass = input("Type L if weight above is in pounds and K if weight above is in kilograms: ")
if mass.upper() == "L":
    weight_kg = weight * 0.45
    print(f"You weigh {weight_kg} kilograms")
else:
    weight_lb = weight / 0.45
    print(f"You weigh {weight_lb} pounds")

