a = eval(input())
b = sorted(a)
b.reverse()
for i in b[0:-1]:
    if i == 0:
        del b[0]
    print(i,end='')
