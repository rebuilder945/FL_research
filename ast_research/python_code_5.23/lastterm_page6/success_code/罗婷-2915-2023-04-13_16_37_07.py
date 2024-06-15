m=int(input())
flag=False
if m<=999:
    for x in range (100,m+1):
        a=x//100
        b=(x-a*100)//10
        c=x%10
        if (a**3+b**3+c**3)==x:
            flag=True
            print(x)
if m>=1000:
    for i in range (100,1000):
        a=i//100
        b=(i-a*100)//10
        c=i%10
        if (a**3+b**3+c**3)==i:
            flag=True
            print(i)   

if flag==False:
    print('none')

