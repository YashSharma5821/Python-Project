print("***************************************WELCOME TO GUESS THE NUMBER******************************************************")
import random
n=random.randint(1,100)
print("There will be total 10 attempts , each wrong attempt will lead to decrease in score")
attempt=10
score=10
while attempt!=0:
    u_guess=int(input("Enter your number "))
    if u_guess<n:
        print("your number is too small")
        score=score-1
        attempt=attempt-1
        print("Your attempt left ",attempt)
    elif u_guess>n:
        print("your number is too large")
        score=score-1
        attempt=attempt-1
        print("Your attempt left ",attempt)
    else:
        print("You guessed it correct ")
        break
print("your total score for the game is ",score ," out of 10 " )
print("Do you want to play more levels ?")
a=int(input(" if yes then write 1 for no write 0 :"))
if a==1:
    for i in range(2,5):
        print("You are playing level ",i)
        if i==2:
            print("Difficulty = Medium")
            print("Here there will be only 5 attempts")
            attempt=5
            score=10
            while attempt!=0:
                u_guess=int(input("Enter your number "))
                if u_guess<n:
                    print("your number is too small")
                    score=score-2
                    attempt=attempt-1
                    print("Your attempt left ",attempt)
                elif u_guess>n:
                    print("your number is too large")
                    score=score-2
                    attempt=attempt-1
                    print("Your attempt left ",attempt)
                else:
                    print("You guessed it correct ")
                    break
                print("your total score for the game is ",score ," out of 10 " )
        elif i==3:
            print("Difficulty = Hard")
            print("Here there will be only 2 attempts")
            attempt=2
            score=10
            while attempt!=0:
                u_guess=int(input("Enter your number "))
                if u_guess<n:
                    print("your number is too small")
                    score=score-5
                    attempt=attempt-1
                    print("Your attempt left ",attempt)
                elif u_guess>n:
                    print("your number is too large")
                    score=score-5
                    attempt=attempt-1
                    print("Your attempt left ",attempt)
                else:
                    print("You guessed it correct ")
                    break
                print("your total score for the game is ",score ," out of 10 " )
        else :
            print("Difficulty = Advanced")
            print("Here there will be only 1 attempts")
            attempt=1
            score=10
            while attempt!=0:
                u_guess=int(input("Enter your number "))
                if u_guess<n:
                    print("your number is too small")
                    score=score-10
                    attempt=attempt-1
                    print("Your attempt left ",attempt)
                elif u_guess>n:
                    print("your number is too large")
                    score=score-10
                    attempt=attempt-1
                    print("Your attempt left ",attempt)
                else:
                    print("You guessed it correct ")
                    break
                print("your total score for the game is ",score ," out of 10 ")
else:
    print("Have a Great Day !")
