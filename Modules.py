import converters
from converters import lbs_to_kg
print(lbs_to_kg(70))

print(round(converters.kg_to_lbs(70), 2))

#####
import maximum
from maximum import find_max
blank = input("> ")
user_list = blank.split(" ")

# convert each item to int type
try:
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])
except ValueError:
    print("Dont put comma after list")  #type error


#alternative code to convert items in the split list from string type to integer type

#user_list = [int(num) for num in user_list]


print(find_max(user_list))
print(max(user_list))