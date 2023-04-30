import random
def out(ls,e):
    f,u=0,0
    for i in ls:
        if i in e[-1]:
            f=1
    for i in ls:
        if i in e:
            print(i,end='')
            continue
        else:
            print('_',end='')
            u+=1
            continue
    print()
    t=(f,u)
    return t
easy=['AND','FIX','OWN','ARE','FLY','ODD','APE','FRY','OUR','ACE','FOR','PET','ACT','GOT','PAT','ASK','GET','PEG','ARM','GOD','PAW','AGE','GEL','PUP','AGO','GAS','PIT','AIR','HAT','PUT','ATE','HIT','POT','ALL','HAS','POP','BUT','HAD','PIN']
medium=['BAKE','WORD','LIST','FOUR','FIVE','NINE','GOOD','BEST','CUTE','ZERO','HUGE','COOL','TREE','RACE','RICE','KEEP','LACE','BEAM','GAME','MARS','TIDE','RIDE','HIDE','EXIT','HOPE','COLD','FROM','NEED','STAY','COME']
hard=['ABOUT','ALERT','ARGUE','BEACH','CARRY','CLAIM','CREAM','DEBUT','ENTRY','FORTH','GROUP','DELAY','EQUAL','FORTY','GROWN','JUDGE','METAL','MEDIA','NEWLY','POWER','RADIO','ROUND','PANEL','PRESS','RAISE','ROUTE','PHASE','PRICE']
print("Welcome to the Hangman Game ".rjust(65))
print("So the theme/story of the hangman game is :".rjust(65))
print('YOU WERE TRAVELLING THROUGH THE WOODS.THEN SOMEONE'.rjust(65))
print('OUT OF NOWHERE HIT YOU ON THE BACK OF YOUR HEAD AND'.rjust(65))
print('WHEN YOU WOKE UP .YOU FOUND OUT THAT A WITCH HAS CAUGHT YOU....'.rjust(65))
print('IN ORDER TO ESCAPE FROM THE WITCH '.rjust(65))
print('YOU MUST GUESS THE CORRECT WORD '.rjust(65))
print('IN ORDER TO SAVE YOURSELF. ANSWER CORRECTLY'.rjust(65))
print('TO SAVE YOURSELD FROM BEING HANGED...'.rjust(65))
print('WILL YOU PLAY?(YES/NO)'.rjust(65))
s=input()
while s in 'YESyes':
    print('YOU CAN PLAY THIS GAME IN || 1: EASY MODE|| 2: NORMAL MODE || 3: HARD MODE'.rjust(40))
    print("1- FOR EASY MODE".rjust(65))
    print("2- FOR NORMAL MODE".rjust(63))
    print("3- FOR HARD MODE".rjust(65))
    n=int(input())
    if n==1:
        word=random.choice(easy)
    elif n==2:
        word=random.choice(medium)
    elif n==3:
        word=random.choice(hard)
    else:
        print('CHOOSE FROM 1,2 OR 3')
        continue
    l=[]
    l.extend(word)
    let=random.choice(l)
    chk=out(l,let)
    c=10
    wrong=[]
    temp2=let
    while c>=0:
        temp=temp2
        print('ENTER YOUR GUESS:')
        s2=input()
        s2=s2.upper()
        temp=temp+s2
        print(temp)
        chk,u=out(l,temp)
        print(chk,u)
        if chk==0:
            temp=''
            wrong.append(s2)
        temp2+=temp
        c-=1
        print('WRONG GUESSES:',*wrong)
        if u==0:
            print('YOU WERE ABLE TO DEFEAT THE WITCH!!!!'.rjust(65))
            print(f'THE WORD WAS:{word}'.rjust(65))
            break
        elif c==9:
            print("         \n"
                  "         \n"
                  "         \n"
                  "       +=====+\n")
            continue
        elif c==8:
            print("        +\n"
                  "        |\n"
                  "        |\n"
                  "     +=====+\n")
            continue
        elif c==7:
            print(" +------+\n"
                  "        |\n"
                  "        |\n"
                  "      +=====+\n")
            continue
        elif c==6:
            print(" +------+\n"
                 " O      |\n"
                  "        |\n"
                  "      +=====+\n")
            continue
        elif c==5:
            print(" +------+\n"
                 " O      |\n"
                 " |      |\n"
                  "     +=====+\n")
            continue
        elif c==4:
            print(" +------+\n"
                 " O      |\n"
                "/|      |\n"
                  "   +=====+\n")
            continue
        elif c==3:
            print(" +------+\n"
                 " O      |\n"
                "/|\     |\n"
                  "   +=====+\n")
            continue
        elif c==2:
            print(" +------+\n"
                 " O      |\n"
                "/|\     |\n"
               "/     +=====+\n")
            continue
        elif c==1:
            print(" +------+\n"
                 " O      |\n"
                "/|\     |\n"
                "/ \  +=====+\n")
            continue
        elif c==0:
            print(" +------+\n"
                  " |      |\n" 
                  " |      |\n"
                  " O      |\n"
                "/|\     |\n"
                 "/ \  +=====+\n")
            print('YOU FAILED TO DEFEAT THE WITCH....'.rjust(65))
            print(f'THE WORD WAS:{word}'.rjust(65))
            break
    s=input("DO YOU WANT TO PLAY AGAIN?(Y/N)".rjust(65))
print("THANKS FOR PLAYING!!!".rjust(65))
