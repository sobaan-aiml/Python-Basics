import random

secret= random.randint(1,10)

guess = int(input("Guess a Random Number From 1 to 10:"))

if guess==secret:
    print("Correct! You Won !!!")
    
else:
    print("You Lost :(  Better Luck Next Time")
    print("The Number was : ", secret)