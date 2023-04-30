s=input("Enter your name :")
print("Welcome to the rock paper scissor game ",s)
print("Rules for the game is :")
print("1. Rock beats Scissor")
print("2. Scissor beats Paper")
print("3. Paper beats Scissor")
ls=["Paper","Rock","Scissor"]
import random
n=random.choice(ls)
a=input("Enter your choice :")
b=a.lower()
if (b=="rock" and n=="scissor") or (b=="paper" and n=="rock") or (b=="scissor" and n=="paper"):
    print("You win.")
elif b==n:
    print("Draw")
else:
    print("Computer Win.")
print("Do you want to play more ?")
x=int(input("If yes write 1 , if no write 0 :"))
if x==1:
    p=int(input("How many times do you want to play ?"))
    while p:
        c=input()
        d=c.lower()
        if (d=="rock" and n=="scissor") or (d=="paper" and n=="rock") or (d=="scissor" and n=="paper"):
            print("You win.")
            p=p-1
        elif d==n:
            print("Draw")
            p=p-1
        else:
            print("Computer Win.")
            p=p-1
else:
    print("Have a good day")
