names = ["John", "Mary", "Mint", "Carol", "Lynn"]
print(names[0:4])
print(names[:])
print(names[1:])
names[0]="Johnny"
print(names)

#Code to find the largest number in a list
numbers = [34,56,17,23,42,99.7888]
maxi = numbers[0]
for num in numbers:
    if num > maxi:
        maxi = num
print(maxi)
maximax= max(numbers)
print(maximax)
roundd=round(numbers[-1], 1)
print(roundd)


###
#2D Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[0][1])
print(matrix[1][2])
matrix[1][1]= 12
print(matrix)

#Using nested loops to iterate over items in 2D lists
for row in matrix:
    for item in row:
        print(item)

###
#List methods
list = [3,5,6,7,8,9,12]
list.append(13) #adds item to list
print(list)
list.insert(0,13) #first indicate index of where you want to add item in list
print(list)
list.remove(8)
print(list)
list.pop() #removes last item in list
print(list)
list.index(12) #check for existence of number in list
print(list)
print(50 in list)  #check for existence of number in list, returns a boolean value
print(list.count(13)) #counts number of time item appears in list
list.sort() #ascending order
list.reverse() #reverse, descending order
print(list)

list2= list.copy()  #create a copy of the list
list.append(17)
print(list)
print(list2)

###Program to remove duplicates in a list
dupli = [1,1,2,3,4,5,6,4,7,8]
uniques = []
for numb in dupli:
    if numb not in uniques:
        uniques.append(numb)
print(uniques)

####
#Tupples :cant add or remove anyting in a pple
numer=(1, 2, 3, 4, 5, 6)
print(numer[3])
#yo can only check index and count in a tupple , thus theyre useful when you create a list and dont want to accidentally change it

#Unpacking can be used for both lists and tupples
unpack = (1, 2, 3)
x,y,z = unpack
print(x)


