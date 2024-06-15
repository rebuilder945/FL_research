list = eval(input())
a,b = eval(input())
c = len(list)
i = a
if i>= 0 and i<c and b>i and b<=c:
    while a>= 0 and b<=c:
        del list[a]
        a = a+1
        if a == b:
            break
    print(list)
else:
    print('error')
