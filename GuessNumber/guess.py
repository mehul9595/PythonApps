print("Guess a number!!")
import random

player_name = input("Enter your name: ")
randomNumber = random.randint(0, 100)
guess = -1
numberOfGuess = 0

while guess != randomNumber:
    guess_input = int(input("Enter a number: "))
    numberOfGuess = numberOfGuess + 1 
    if guess_input > randomNumber:
        print("Guess is too high")
    elif guess_input < randomNumber: 
        print("Guess is too low")
    elif guess_input == randomNumber:
        print("Hooray!, You guessed it right!.")
        print("{} guessed in {} tries".format(player_name, numberOfGuess))
        break

print("Game over!")