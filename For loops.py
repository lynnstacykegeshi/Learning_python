for item in "Stacy":
    print(item)

for item in ["lynn", "Stacy", "Wendy"]:
        print(item)

for item in range(12,67,3):
    print(item, end=" ")
print()

basket = [10, 20, 30]
total = 0
for price in basket:
    total += price
print(f"Items in basket cost {total}")

total=0
for item in range(11):
    total += item
    print(total)



###
#Nested loops
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

#Create a rectangle
rows= int(input("Number of rows " ))
columns = int(input("Number of columns "))
symbol = input("Enter a symbol to use ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

numbers1 = [5,2,5,2,2]
for ncount in numbers1:
    print(ncount * "X")

numbers2= [1,1,1,1,6]
for ncount in numbers2:
    output =""
    for count in range(ncount):
        output += "X"
    print(output)

