a = eval(input())
b = sorted(a)
b.reverse()
for i in b:
    if i == 0:
        print(0)
    else:
        break
    print(i,end='')
