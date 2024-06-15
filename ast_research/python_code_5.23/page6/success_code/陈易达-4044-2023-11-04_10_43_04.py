n = eval(input())
if n <= 100:
    print('None')
else:
    ls = []
    for x in range(100,n+1):
        a = int(str(x)[0])
        b = int(str(x)[1])
        c = int(str(x)[2])
        if a**3+b**3+c**3 == x:
            print(x)
            ls.append(x)
    if len(ls) == 0:
        print('None')

