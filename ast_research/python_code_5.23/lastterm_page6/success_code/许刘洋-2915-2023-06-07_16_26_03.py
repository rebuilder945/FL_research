a=eval(input())
for i in range(a+1):
    if (i%10)**3+(i//10%10)**3+(i//100)**3==i and 100<=i<=999:
        print(i)
else:
    print('None')

