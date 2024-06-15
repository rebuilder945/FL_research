m=eval(input())
if m<153:
    print('none')
else:
    for s in range(100,m+1):
        a=s%10
        b=s//10%10
        c=s//100
        x=a**3+b**3+c**3
        if s==x:
            print(s)
        else:
            pass
