n=eval(input())
for i in range(100,n):
    if i<=1000:
        a=i//100
        b=(i-a*100)//10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)
    elif i>1000:
        pass
        
