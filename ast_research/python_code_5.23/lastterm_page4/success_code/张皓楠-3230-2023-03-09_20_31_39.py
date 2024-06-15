a = eval(input())
b = sorted(a)
b.reverse()
for i in b:
    if not i == 0:
        break
    print(i,end='')


