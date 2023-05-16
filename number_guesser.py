import random

random_number = random.randint(0, 100)

while True:
    user_guess = input("Guess a number from 1 to 100: ")
    if not user_guess.isdigit():
        print('Please type a number next time. ')
        continue

    user_guess = int(user_guess)

    if user_guess < 0 or user_guess > 100:
        print("Please enter a number within the range of 0 to 100")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
