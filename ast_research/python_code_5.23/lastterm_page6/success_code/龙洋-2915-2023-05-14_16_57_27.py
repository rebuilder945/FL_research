x=eval(input())
if x <=100:
    print('none')
else:
    for n in range(100,x+1):
        ge=n%10
        shi=(n-ge)*0.1%10
        bai=n//100
        if ge**3+shi**3+bai**3==n and n<1000:
            print(n)
