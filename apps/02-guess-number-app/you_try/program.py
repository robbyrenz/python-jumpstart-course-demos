import random  # I have to import the random library/module

print()
print('--------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('--------------------------------------')
print()

the_number = random.randint(0, 100)  # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

user_name = input('Please enter your name: ')
guess_text = int(input('Guess a number between 0 and a 100: '))

while guess_text != the_number:
    if guess_text < the_number:
        print('Sorry, the number you guessed is LOWER than the actual number')
        guess_text = int(input('Guess a number between 0 and a 100: '))
    else:
        print('Sorry, the number you guessed is HIGHER than the actual number')
        guess_text = int(input('Guess a number between 0 and a 100: '))

print()
print(f'CONGRATULATIONS, {user_name}! You guessed the right number!!!')
