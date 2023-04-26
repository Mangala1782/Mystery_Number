# Date: 04 - 26 - 2023
# Name: Xaiver Hickey
# Project Name: Number Mystery 


# Imports 
import random

# Var
attempts = 0

# Number generator
number = random.randint(1,100)
userNum = 0

while (userNum != number):
    #input 
    userNum = int(input("Please guess a number from 1 to 100: "))

    if userNum > number: # Too high
        message = "Number too high!"
        attempts += 1
    
    elif userNum == number: # Victory
        print("==][================][==")
        print("You guessed the number!")
        print("==][================][==")
        input('Press ENTER to exit')
    
    else: # Too low 
        message = "Number too low!"
        attempts += 1
  
    print()
    print(message)

    # Display attempts
    print()
    print("Attempts Made: ", attempts)
    print("==][================][==")
