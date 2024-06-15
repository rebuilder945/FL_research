n = eval(input())
if n <= 100:
    print('none')
elif n <= 999:
    for i in range(100,n+1):
        i = str(i)
        a = i[0]
        b = i[1]
        c = i[2]
        if int(a)**3+int(b)**3+int(c)**3 == int(i):
            print(i)
else:
    for i in range(100,1000):
        i = str(i)
        a = i[0]
        b = i[1]
        c = i[2]
        if int(a)**3+int(b)**3+int(c)**3 == int(i):
            print(i)


