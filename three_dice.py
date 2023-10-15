import random
import sys


def game(number_list):
    for i in range(3):
        number_list[i] = random.randint(1, 6)
        print(number_list[i])
        if i < 2:
            print("*")

    print("--------")
    answer = result(number_list)
    guessing_game(answer)


def result(number_list):
    return number_list[0] * number_list[1] * number_list[2]


def guessing_game(the_answer):
    while True:
        try:
            guess = int(input("What is your answer? Type the number or 0 to restart the game: "))
        except ValueError:
            print("You need to enter a number.")
        else:
            if guess == the_answer:
                print("You won!")
                break

            elif guess == 0:
                break

            else:
                print("Wrong answer. Please try again.")


def main():
    number_list = [0, 0, 0]
    while True:
        print("Welcome to the Three Dice Game. Enter 1 to play, R to see Game rules or Q to quit.")
        user_input = input("Enter here: ")

        if user_input == "1":
            game(number_list)
        elif user_input.upper() == "R":
            print("When the game starts, three dice are rolled. Your mission is to provide the result of multiplying these three numbers together.")
        elif user_input.upper() == "Q":
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
