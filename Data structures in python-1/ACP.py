import random

number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!!")
print("Guess the number between 1 and 100")

attempts = 0

while True:
    attempts += 1

    guess = int(input("What's your guess: "))

    if guess < number_to_guess:
        print("Too low")

    elif guess > number_to_guess:
        print("Too high!")

    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts")
        break
