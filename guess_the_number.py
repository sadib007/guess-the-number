import random


# returns the random integer between x and y including x and y
def generateRandomNumber(x: int, y: int) -> int:
    return random.randint(x, y)


random_number = generateRandomNumber(1, 100)
attempt = 0  # attempt counter
user_input = 0  # varraible to hold user input

while (random_number != user_input):
    x = input("Please enter the number you guess. Enter q to quit the game: ")
    if (x.lower() == 'q'):  # control to check if user decided to quit
        exit()
    try:
        user_input = int(x)  # convert entered user input from string to int
    except ValueError as e:  # catch exception if user enters anything else other than an integer number
        print("The entered input is not an integer number. Please enter an integer number.")
        continue
    attempt += 1    # increase attempt counter
    if user_input > random_number:
        # entered number is higher than the guess
        print("Your guess is too high.")
    else:
        # entered number is lower than the guess.
        print("Your guess is too low.")

print(
    f"You needed {attempt} attemps to guess the correct number {random_number}.")  # final result
