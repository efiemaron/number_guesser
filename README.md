# number_guesser
he code imports the random module, which provides functions for generating random numbers.
The random.randint(0, 100) function is used to generate a random integer between 0 and 100, inclusive. This number is assigned to the variable random_number.
The code enters a while loop that continues indefinitely until the user guesses the correct number.
Inside the loop, the user is prompted to enter a guess by using the input() function. The input is stored in the variable user_guess.
The code checks if the input is a valid number by using the isdigit() method. If the input is not a number, an error message is displayed, and the loop continues to the next iteration using the continue statement.
If the input is a number, it is converted to an integer using the int() function and stored back in the user_guess variable.
The code checks if the user's guess is outside the range of 0 to 100. If it is, an error message is displayed, and the loop continues to the next iteration.
If the user's guess matches the random number, the code displays a success message, "You got it!", and exits the loop using the break statement.
If the user's guess is not equal to the random number, the code checks if the guess is higher or lower. It displays either "You were above the number!" or "You were below the number!" accordingly.
The loop continues to the next iteration, prompting the user for another guess.
