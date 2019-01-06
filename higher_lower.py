import random


# Main module, flow of program
def main():
    player = get_player_name()
    number = house_number()
    name, tries = game(player, number)
    high_score(name, tries)
    run_again()


# This gets the player's name and returns it as a string
def get_player_name():
    player = input("Enter your name: ")
    player = player.upper()

    return player


# this get the computer's secret number and returns it as an integer (1-100)
def house_number():
    number = random.randint(1, 100)

    return number


# this is the GAME Function. It has ' player_name ' as an argument and ' number ' .  It returns 'player_name' and 'number_of_guesses'
def game(p, n):
    num_of_guesses = 0 # this counts the guesses

    print("Hello", p, '\n')
    player_number = int(input("Choose a number between 1 and 100: "))
    if player_number != p:
        num_of_guesses += 1  # if first choice is not the answer, +1 in number of guesses

    while player_number != n:  # This loop will go until the number is guesses
        num_of_guesses += 1  # Adding 1 to 'number_of_guesses' every time it is not the number

        if player_number < n:  # The IF and ELIF tells you if the secret number is higher or lower than your guess
            print('The secret number is higher than', player_number, '\n')
            player_number = int(input("Choose a number between 1 and 100: "))
        elif player_number > n:
            print('The secret number is lower than', player_number, '\n')
            player_number = int(input("Choose a number between 1 and 100: "))
    print('BOOM!  You guessed it in', num_of_guesses, 'tries')

    return p, num_of_guesses


# This takes the name and amount of guesses as arguments.  It doesn't update if you run again.  It replaces.
def high_score(n, t):
    high_scores = {n: t}
    print(high_scores)


#  This asks the user if they want to play again.  If they select yes, it starts the main() module
def run_again():
    again = input('Play again? [y/n] ')
    while again != 'y' or again != 'n':
        if again == 'y':
            main()
        elif again == 'n':
            quit()


main()
