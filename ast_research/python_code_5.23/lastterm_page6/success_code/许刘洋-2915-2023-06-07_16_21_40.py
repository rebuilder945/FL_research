a=eval(input())
for i in range(100,a+1):
    if (i%10)**3+(i//10%10)**3+(i//100)**3==i:
        print(i)


