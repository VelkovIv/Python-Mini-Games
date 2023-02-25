import random
from colorama import Fore, Style


class Game:
    def __init__(self, max_attempts=3):
        self.number = random.randint(1, 10)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.won = False

    def guess(self, number):
        self.attempts += 1

        if number == self.number:
            self.won = True
            print(Fore.GREEN, '\nCongratulations, you won!')
            print(Style.RESET_ALL)

        elif number < self.number:
            print('The number is higher than your guess. Try again!')
        else:
            print('The number is lower than your guess. Try again!')

        if self.attempts == self.max_attempts and not self.won:
            print(Fore.RED, f'\nSorry, you lost.The number is {self.number}')
            print(Style.RESET_ALL)


# Welcome to the game
print(Fore.BLUE, '#' * 45)
print(Fore.BLUE, '# ', end="")
print(Fore.YELLOW, 'Welcome to the Game - "Guess the Number"', end='')
print(Fore.BLUE, '#')
print(Fore.BLUE, '#' * 45, end='')
print(Style.RESET_ALL)
while True:
    # Game start
    game = Game()
    while not game.won and game.attempts < game.max_attempts:
        number = int(input('\nGuess a number between 1 to 10: '))
        game.guess(number)
    # Choose a new game or exit
    exit_check = input('Do you want to play again? (y/n): ')
    if exit_check.lower() == 'n':
        print(Fore.CYAN, 'Thank you! Bye!')
        print(Style.RESET_ALL)
        break
