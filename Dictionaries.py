customer = {
    "name":"John Smith",
    "age":30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("Birthdate"))
print(customer.get("Birthdate", "NA"))
customer["name"]="Jack Smith"
print(customer)

number = {
    "1": "One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
blank = input("Phone number: ")
outputstr = ""

for digit in blank:
    outputstr+= number.get(digit, "NA")+ " "
print(outputstr)

####
#Emoji converter
message= input("> ")
output1=" "
words = message.split()
emojis={
    ":)": "😊😊",
    ";)": "😉😉",
    ":(": "😥😥"
}
for text in words:
    output1 += emojis.get(text, text) +" "
print(output1)
