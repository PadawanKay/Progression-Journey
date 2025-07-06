import random

# Rules/key starts here:
def answer():
    random.seed(5)
computer_number = random.randrange(1, 5)
max_attempts, attempts = 3, 0

# Game code starts here:
name = input("What's your name? ")
print("Hello, " + name)
user_input = input("Do you want to play a game? ")

if user_input == 'yes':
    print("Good Choice!")
    print("You have 3 attempts to guess my number!")
    print("Hmmm, I'm thinking of a number between 1 and 5!")
    print("Can you guess it, " + name)
    while attempts < max_attempts:
        guess = input("Type your guess here: ")
        if guess == f"{computer_number}":
            print(f"The number I was Thinking of was {computer_number}")
            print("Winner Winner Chicken Dinner!")
            print("I hope you have a great rest of your day!")
            print("Oh, I almost forgot! Thank you for playing!")
            break
        elif attempts < max_attempts:
            print("Another one bites the dust! Try Again!")
            attempts += 1
            pass
        if attempts == max_attempts:
            print(f"The number I was Thinking of was {computer_number}")
            print("AH! I wasn't supposed to win!")
            print("Please play again!")

else:
    print("Oh...")
    print("Maybe next time, " + name)
    print("Goodbye!")

#Remember:
# Even though it took manyhours to figure out, think about how happy you felt when you solved each problem!
# Struggle = Growth <3
