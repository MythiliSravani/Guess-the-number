import random

secretNumber = random.randint(1, 20)
print('guess the secret number in my mind')
print('you will get only five guesses think wisely')
print('game starts now please input your guesses')
for i in range(1, 6):
    myGuess = int(input())
    if myGuess > secretNumber:
        print('you overestimated my secret number')
    elif myGuess < secretNumber:
        print('you underestimated my secret number')
    else:
        break
if myGuess == secretNumber:
    print('Alas! you guessed it')
else:
    print('Better luck next time')

