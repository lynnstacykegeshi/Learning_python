
#While loops
i=1
while i<= 5:
    print("#"* i)
    i=(i+1)
print("Done")

#Guessing game
win_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == win_no:
        print("You win")
        break
else:
    print("You lose")





###
#Car game
help="""
start - To start the game
stop - To stop the game
quit - To exit the game"""

command = ""
started = False #initially our car is stopped

while True:
    command = input("> ").lower() # to eliminate duplicate in the codes following
    if command == "start":
        if started :
            print("Car is already started")
        else:
            started = True
            print("Car has started")
    elif command == "stop":
        if not started:
            print("Car has already stopped")
        else:
            started = False
            print("Car has stopped")
    elif command == "help":
        print(help)
    elif command == "quit":
        break
    else:
        print("Computer does not understand the characters")


