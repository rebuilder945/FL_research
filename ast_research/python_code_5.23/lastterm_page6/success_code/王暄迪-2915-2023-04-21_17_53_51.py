n=int(input())
s=0
if n>=100 and n<=999:
    x=100
    if x<=100:
        a=x%10
        b=x//10%10
        c=x//100
        if x==a**3+b**3+c**3:
            print(x)
            x+=1
        else:
            s+=1
            x+=1
    else:
        pass
    if s==0:
        print("none")
