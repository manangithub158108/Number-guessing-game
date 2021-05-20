# settng up the user enviroment
print('Number guessing game')
print('Guess any number between 1 to 9');

import random
randomNum = random.randint(1, 9);

# creating the main functionality
chances = 0;
while chances >= 0 and chances <= 5 :
    
    guess = int ( input ('Enter your guess'));
    
    if guess > randomNum :
        print('Your guess was too high, Guess a number lower than your expectation');
    elif guess < randomNum and chances  :
        print('Your guess was too low, Guess a number higher than your expectation');
    else :
        print('Yahoo!! you guessed the correct number');

    chances = chances + 1;

    if chances == 6 :
        print('You have done well, thank you')
