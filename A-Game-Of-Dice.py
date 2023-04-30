import random
number_of_throws=int(input('How many times do you want to throw the dice: ',))
for i in range(1,number_of_throws+1):
    ls=random.choice(['1','2','3','4','5','6'])
    print(f'Your {i} time attempt throw of dices is:')
    print(f'''
              ______
             |      |
             |  {ls}   |
             |______|   ''')
    number_of_throws-=1

