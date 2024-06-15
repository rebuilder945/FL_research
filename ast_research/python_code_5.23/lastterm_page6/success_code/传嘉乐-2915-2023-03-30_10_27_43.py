x=eval(input())
if x<153:
    print('none')
elif x>1000:
    for a in range(100,1000):
        if a==(a//100)**3+((a%100)//10)**3+(a%10)**3:
            print(a)
else:
    for a in range(100,x+1):
        if a==(a//100)**3+((a%100)//10)**3+(a%10)**3:
            print(a)

