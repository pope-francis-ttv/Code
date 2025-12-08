import random

secret = random.randint(0,20)

while True:
    guess = int(input("enter guess: "))
    if guess > secret:
        print('Too high! Try again')
    elif guess < secret:
        print('Too low! Try again')
    else:
        print('You got it!')
        break
    