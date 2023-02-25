import random
from colorama import Fore, Style

command = ''
while command != 'n':
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'
    player_move = input('Choose: [r]ock, [p]aper or [s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid input. Try again ...')  # raise SystemExit('Invalid input. Try again ...')
        continue

    computer_random_number = random.randint(1, 3)

    computer_move = ''
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f'The computer chose {computer_move}')

    if player_move == rock and computer_move == scissors or \
            player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        print(Fore.GREEN, 'You win!')
        print(Style.RESET_ALL)
    elif player_move == computer_move:
        print(Fore.YELLOW, 'Draw')
        print(Style.RESET_ALL)
    else:
        print(Fore.RED, 'You lose!')
        print(Style.RESET_ALL)
    command = input('New gane [y]es or [n]: ')
else:
    print('Thank you! Bye!')
