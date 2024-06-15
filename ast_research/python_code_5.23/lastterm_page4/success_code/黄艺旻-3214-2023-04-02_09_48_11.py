a = eval(input())
for i in range(len(a)):
    if a[i] == 0:
        a[i] = a[-1]
        print(a)
