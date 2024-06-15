a=eval(input())
if a>=135:
    for i in range(101,a+1):
        d=i//100
        b=(i//10)%10
        c=i%10
        if b**3+d**3+c**3==i:
            print(i)
elif a<135:
    print('none')

