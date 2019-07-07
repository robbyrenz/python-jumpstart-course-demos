# a program that asks the user to guess what number the computer chose between 1 and a 100, inclusively
# this program also demonstrates the three ways that I know of concatenating strings with variables

import random  # so that I can use the random library/module

print()
print('------------------------------------------------')
print('           GUESS THE NUMBER GAME')
print('------------------------------------------------')
print()

number = random.randint(1, 100)  # chooses a random number between 1 and 100, inclusively
guess_number = -1
name = input('What is your name? ')

while guess_number != number:

    guess_number_string = input('Guess a number between 1 and a 100: ')
    guess_number = int(guess_number_string)  # parse the variable to an int

    if guess_number < number:
        print('Sorry {1}, the number {0} was LOWER than the actual number!\n'.format(guess_number, name))
    elif guess_number > number:
        print('Sorry {}, the number {} was HIGHER than the actual number!\n'.format(name, guess_number))
    else:
        break

print()
print(f'Congratulations {name}, the number {guess_number} was what the computer was thinking!')
print('\t\t\t************PROGRAM ENDED***************')
