import random

correct_number = random.randint(1, 100)
guess = None  

print("Welcome to the my little game^_^ ")
print("I've got a number in my head between 1 and 100. Can you guess what it is?")

while guess != correct_number:
    try:
        guess = int(input("Enter your guess: "))
      
        if guess < correct_number:
            print("Too low!")
        elif guess > correct_number:
            print("Too high!")
        else:
            print("Woohoo! You guessed my number correctly^_^.")
    except ValueError:
        print("Please enter a valid number.")


