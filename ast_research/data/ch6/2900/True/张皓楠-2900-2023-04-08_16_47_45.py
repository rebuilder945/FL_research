a = eval(input())
b = []
c = []
d = []
if type(a) is not int or a < 2:
    print("illegal input")
else:
    for i in range(2,a+1):
        if str(i) == str(i)[::-1]:
            b.append(i)
    for i in b:
        for j in range(2,i):
            if i%j == 0:
                c.append(i)
    for i in b:
        if i not in c:
            print(i,end = " ")


