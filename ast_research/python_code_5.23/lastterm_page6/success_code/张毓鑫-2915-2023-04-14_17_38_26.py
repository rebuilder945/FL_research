a=eval(input())
e=0
if a>=153:
    for i in range(100,a+1):
        d=i//100
        b=(i//10)%10
        c=i%10
        if b**3+d**3+c**3==i:
            print(i)
elif a<153:
    print('none')

