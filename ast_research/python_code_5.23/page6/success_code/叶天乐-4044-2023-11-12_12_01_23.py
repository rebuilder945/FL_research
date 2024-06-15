a = eval(input())
for i in range(0,a):
    if (a//100)**3+(a//10%10)**3+(a%100)**3==i:
        print(i)
else:
    print("none")
