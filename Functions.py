#greet_user is a function, inside the parenthesis you can add parameters which are place holders for receiving informatio
def greet_user(name):
    print(f"Hi {name}")
    print("Crochet world"),
    print("Make all your patterns come to life")


print("Open page")
greet_user("Stacy")
greet_user("Lynn")
print("Click next")


#name is a parameter and Lynn and Stacy are the arguments that we pass to the name parameter
#parameters are place holder
#arguments are the actual piece of information being passed


#positional arguments, their position matters
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to crochet world"),
    print("Make all your patterns come to life")

print("Open page")
greet_user("Stacy" ,"Jean")
greet_user("Lynn", "Wambui")
print("Click next")

#Key word arguments, their position does not matter

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to crochet world"),
    print("Make all your patterns come to life")


greet_user(first_name="Winter",last_name= "Wambui")

#When using funtions with multiple numerical values then use key word arguments to improve readability
#if you're passing both positional and key word arguments, use key word arguments after positional argument

####
#Return Statements (works like input function
def square(number):
    return number*number

print(square(15))

def multiply(number1, number2):
    return number2 * number1


print(multiply(6,8))

#Creating a reusable function
#Extract function from the emoji converter
def emoji_converter(message):
    output1 = " "
    words = message.split(" ")
    emojis = {
        ":)": "😊😊",
        ";)": "😉😉",
        ":(": "😥😥"
    }
    for text in words:
        output1 += emojis.get(text, text) + " "
    return output1

message = input(">")
print(emoji_converter(message))