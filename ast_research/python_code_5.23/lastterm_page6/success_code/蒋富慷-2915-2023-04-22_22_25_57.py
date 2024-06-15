a = eval(input())
b = 0
for x in range(a+1):
    for i in str(x):
        b += int(i)**3
        if b == x:
            print(b)
