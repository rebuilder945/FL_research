a=int(input())
for x in range(100,a+1):
    if (x%10)**3+(x//10%10)**3+(x//100%10)**3==x:
        print(x)
    else:
        pass


