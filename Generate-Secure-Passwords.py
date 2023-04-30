import random
p=int(input('''Enter 1 for generating 8 character  password
Enter 2 for generating 9 character  password
Enter 3 for generating 10 character password
Enter 4 for generating 11 character password
Enter 5 for generating 12 character password: '''))
if p==1:
    sequence=''
    for i in range(8):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('Your 8 character sequence password is: ',sequence)
elif p==2:
    sequence=''
    for i in range(9):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('Your 9 character sequence password is: ',sequence)
elif p==3:
    sequence=''
    for i in range(10):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('Your 10 character sequence password is: ',sequence)
elif p==4:
    sequence=''
    for i in range(11):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('Your 11 character sequence password is: ',sequence)
elif p==5:
    sequence=''
    for i in range(12):
        r=random.randint(65,122)
        sequence+=chr(r)
    print('Your 12 character sequence password is: ',sequence)
