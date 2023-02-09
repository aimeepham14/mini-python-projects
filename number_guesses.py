import random

# print(random.randrange(start, stop))
# for stop need to put one count extra

#one method
# r = random.randrange(-5, 11)
# print(r)

#second method
# r = random.randint(-5, 11)
# print(r)

top_of_range = input("Type a number: ")
#how to convert a number that a user types in from a string to a number. It HAS to be a digit, with is digit method
# example: int("25") -> 25

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
#this is the guesses counter
guesses = 0

#now it's time to match whatever the user's input is with what the computer generated
while True:
    guesses += 1
    user_guess = input("Make a guess: ")    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        #this continue brings us back to the top of the loop
        continue

    if user_guess == random_number:
        print("You got it!")
        #this breaks the loop
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")