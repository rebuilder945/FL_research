s={1:"spring",2:"summer",3:"autumn",4:"winter"}
a=int(input())
if a in (3,4,5):
    print(s[1])
elif a in (6,7,8):
    print(s[2])
elif a in (9,10,11):
    print(s[3])
elif a in (1,2,12):
    print(s[4])
else:
    print("error")

