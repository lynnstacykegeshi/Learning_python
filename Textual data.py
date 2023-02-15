message = "Good morning"
print(message)
print(len(message))
print(message[ :4])
print(message[5:])
print(message.lower())
print(message.upper())
print(message.count("o"))
print(message.find("morning"))
new_message= message.replace("morning", "afternoon")
print(new_message)

greeting="Hello"
name= "stacy"
message= greeting + ", " +  name +  ".  Welcome!"
print(message)

message2="{},{}.Welcome!".format(greeting,name)
print(message2)

message3 =  f'{greeting}, {name.upper()}. Welcome!'
print(message3 * 3)

#print(help(str))