import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))

    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print("Correct!")
        break
