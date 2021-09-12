import random 

print ("number guessing game")

number = random.randint (1,9)

chances = 0 

print ("guess a number between 1 and 9:")

while chances <5 :
    guess = int (input("Enter your number:"))

    if guess == number:
        print ("You won!")
        break 
    elif guess < number :
        print ('your guess is lower than the number: Guess a number higher  ', guess)
    else :
        print('your guess was higher than the number : Guess a number lower than ', guess)

chances += 1 

if not chances <5 :
    print ("You lost! The numebr is " , number)