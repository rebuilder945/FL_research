n=eval(input())
if n<=152 and n>=1001:
    print(None)
else:
    
    for i in range(2,n+1):
        a=i%10
        b=i//10%10
        c=i//100
        if a**3+b**3+c**3==i:
            print(i)
        

