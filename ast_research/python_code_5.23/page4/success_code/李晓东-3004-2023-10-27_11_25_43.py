a = eval(input())
for i in a:
    if 1 in a:
        a.remove(1)
    elif i>=2:
        for x in range(2,i):
            if i%x ==0:
                a.remove(i)
                print(a)





