a = eval(input())
for i in range(0,a):
    if (i//100)**3+(i//10%10)**3+(i%100)**3==i:
        print(i)
else:
    print("none")
