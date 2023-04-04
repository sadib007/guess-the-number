# Md Shaberul hoque
# Matriculation number_3091806

import random
import winsound
from datetime import datetime, timedelta

# returns the random integer between x and y including x and y


def generateRandomNumber(x: int, y: int) -> int:
    return random.randint(x, y)


def printTimer(inception: datetime) -> str:
    now = datetime.now()
    return (now-inception).seconds


random_number = generateRandomNumber(1, 100)
attempt = 0  # attempt counter
user_input = 0  # varraible to hold user input
start_time = datetime.now()
while (random_number != user_input):
    x = input("Please enter the number you guess. Enter q to quit the game: ")
    if (x.lower() == 'q'):  # control to check if user decided to quit
        exit()
    try:
        user_input = int(x)  # convert entered user input from string to int
    except ValueError as e:  # catch exception if user enters anything else other than an integer number
        winsound.MessageBeep(winsound.MB_OK)

        print(
            f"The entered input is not an integer number. Please enter an integer number. Elapsed Time: {printTimer(start_time)}s")
        continue
    attempt += 1    # increase attempt counter
    if user_input > random_number:
        # entered number is higher than the guess
        winsound.MessageBeep(winsound.MB_OK)
        print(
            f"Your guess is too high. Elapsed Time: {printTimer(start_time)}s")
    else:
        # entered number is lower than the guess.
        winsound.MessageBeep(winsound.MB_OK)
        print(
            f"Your guess is too low. Elapsed Time: {printTimer(start_time)}s")

winsound.MessageBeep(winsound.MB_OK)
print(
    f"You needed {attempt} attemps to guess the correct number {random_number}. Elapsed Time: {printTimer(start_time)}s")  # final result
