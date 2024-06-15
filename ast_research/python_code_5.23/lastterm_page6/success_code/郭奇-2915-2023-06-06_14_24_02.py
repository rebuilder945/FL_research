n=int(input())
if n>100 and n<=1000:
    for i in range(100,n+1):
        a=i//100
        b=(i//10)%10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)
        
else:
    print('none')

 
