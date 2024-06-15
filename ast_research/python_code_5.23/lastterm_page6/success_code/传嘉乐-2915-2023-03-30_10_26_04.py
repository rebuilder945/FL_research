x=eval(input())
if x<=153:
    print('none')
else:
    for a in range(100,x):
        if a==(a//100)**3+((a%100)//10)**3+(a%10)**3:
            print(a)

