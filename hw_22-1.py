import random


def new_game():
    computer_choice = random.randint(1, 10)
    user_choice = 0

    while user_choice != computer_choice:
        user_choice = input('Guess the number from 1 to 10 (\'q\' for exit):')
        if user_choice == 'q':
            print('Bye!')
            break

        if not user_choice.isnumeric():
            print('Invalid data!')
            continue

        user_choice = int(user_choice)
        if not (1 <= user_choice <= 10):
            print('Invalid data!')
            continue
        if user_choice == computer_choice:
            print('Congratulations!!! You guessed the figure!')
            break
        elif user_choice < computer_choice:
            print('Try again! The right number is greater:')

        else:
            print('Try again! The right number is smaller:')




new_game()