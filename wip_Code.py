from random import randrange
# Note-to-self: pick FROM class then IMPORT subclass....

max_attempts, attempts = 3, 0


name = input("What's your name? ")
print("Hello, " + name)

user_input = input("Do you want to play a game? ")
if user_input == 'yes':
    print("Good Choice!")
    print("Hmmm, I'm thinking of a number between 1 and 50!")
    print("Can you guess it, " + name)
    while attempts < max_attempts:
        input("Type your guess here: ")                                    # Research attempts for the initial guess instead of
        print("The number I'm thinking of is ", end= "")                   # resetting the rng number each time the guess is wrong.
        print(randrange(1, 50, 1))
        if user_input == 'correct':
            print("Winner Winner Chicken Dinner!")
            print("I hope you have a great rest of your day!")
            print("Oh, I almost forgot! Thank you for playing!")
            break
        elif attempts < max_attempts:
            print("Another one bites the dust! Try Again!")
        attempts += 1
    if attempts == max_attempts:
        print("AH! I wasn't supposed to win!")
        print("Please play again!")
else:
    print("Oh...")
    print("Maybe next time, " + name)
    print("Goodbye!")

#Remember:
# Even though it took MANY hours to figure out, think about how happy you felt when you solved each problem! 
# From trying to get Python on Github to building a fun Guessing Game!
# Struggle = Growth <3
