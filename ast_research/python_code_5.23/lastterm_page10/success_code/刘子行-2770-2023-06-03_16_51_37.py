def fuck(a,b):
    a1=set(a)
    b1=set(b)
    if a==b:
        return True
    else:
        return False
ass=input()
boob=input()
if ass.isalpha():
    print(fuck(ass,boob))
else:
    print('False')

