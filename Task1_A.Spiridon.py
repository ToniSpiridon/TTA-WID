import random
number = random. randint(0, 10)
print(number)

myName = input ("What is your name? ")

print("Hello " + myName)
print("I am thinking of a number between 1 to 10. Can you guess it? ")

print('Well, ' + myName + ', I am thinking of a number between 1 and 10.')

print('Take a guess.') # There are four spaces in front of print.
guess = input()
guess = int(guess)

if guess < number:
print('Your guess is too low.')

if guess > number:
print('Your guess is too high.')

if guess == number:
print('Good job, ' + myName + '! You guessed my number!')

if guess == number:
print('Nope. The number I was thinking of was ' + number)