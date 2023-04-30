import random
alphanum=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['0','1','2','3','4','5','6','7','8','9']
s=input('DO YOU REQUIRE AN OTP/CAPTCHA?(Y/N) :')
while s in 'YESyes':
    co=[4,6]
    ptp=random.choice(co)
    if ptp==4:
        print('ENTER CAPTCHA GIVEN BELOW')
        c=''
        for i in range(ptp):
            c+=random.choice(alphanum)
        print(c)
        s2=input()
        if s2==c:
            print("AUTHENCIATION SUCCESSFUL")
            break
        else:
            print('AUTHENCIATION UNSUCCESSFUL... REFRESHING PAGE')
            pass
    if ptp==6:
        o=''
        for i in range(ptp):
            o+=random.choice(num)
        print("OTP:",o)
        print('ENTER OTP')
        s2=input()
        if s2==o:
            print('AUTHENCIATION SUCCESSFUL')
            break
        else:
            print("AUTHENCIATION UNSUCCESSFUL... REFREAHING PAGE")
            continue
print("HEADING TO DESIRED WEBPAGE.....")
