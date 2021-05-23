import random

RandomNumber = random.randint(0,10)

Chances = 0

while Chances < 5 :
    GuessedNumber = int(input("Guess a random number between 0 and 10, and I will tell you whether it is the same as the number that I have guessed. You get 5 chances."))
    if GuessedNumber == RandomNumber :
        print("This answer is correct!")
        break
    elif not GuessedNumber == RandomNumber :
        print("Sorry, but the number is incorrect.")
        Chances = Chances + 1
        if not Chances < 5 :
            print("You lose. The number is", RandomNumber, ".")