#!python3
import random
import logging
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
guess = ''
sides = ('heads', 'tails')
print('Guess the coin toss! Enter heads or tails:')
guess = input().lower()
logging.debug("The user guessed " + guess)

attemptNum = 0
toss = sides[random.randint(0, 1)] # 0 is tails, 1 is heads
logging.debug("Toss is " + toss)
while True:

    if guess not in sides:
        raise Exception('"{0}" is an invalid guess. You must guess "heads" or "tails"'.format(guess))

    if toss == guess:
        print('You got it!')
        break
    elif attemptNum < 1:
        print('Nope! Guess again!')
        attemptNum += 1
        guess = input()
    else:
        print("You are really bad at this game")
        break