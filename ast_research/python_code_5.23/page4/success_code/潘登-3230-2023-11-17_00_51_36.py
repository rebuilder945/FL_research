a=eval(input())
a.sort()
a.reverse()
for x in range(len(a)):
    if x == 0:
        print("0")
    else:
        print(a[x],end='')
