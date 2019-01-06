import random


def main():
    player = get_player_name()
    number = house_number()
    name, tries = game(player, number)
    high_score(name, tries)
    run_again()


def get_player_name():
    player = input("Enter your name: ")
    player = player.upper()

    return player


def house_number():
    number = random.randint(1, 100)

    return number


def game(p, n):
    num_of_guesses = 0

    print("Hello", p)
    player_number = int(input("Choose a number between 1 and 100: "))

    while player_number != n:
        num_of_guesses += 1

        if player_number < n:
            print('The secret number is higher than', player_number)
            player_number = int(input("Choose a number between 1 and 100: "))
        elif player_number > n:
            print('The secret number is lower than', player_number)
            player_number = int(input("Choose a number between 1 and 100: "))
    print('BOOM!  You guessed it in', num_of_guesses, 'tries')

    return p, num_of_guesses


def high_score(n, t):
    high_scores = {n: t}
    print(high_scores)


def run_again():
    again = input('Play again? [y/n] ')
    while again != 'y' or again != 'n':
        if again == 'y':
            main()
        elif again == 'n':
            quit()


main()
