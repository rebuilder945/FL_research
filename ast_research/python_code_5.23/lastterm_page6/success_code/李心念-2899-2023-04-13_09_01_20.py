n = [eval(x) for x in input().split()]
a = n[0]
b = n[1]
def zuhe(list):
    lst = []
    a,b,c = list[0],list[1],list[2]
    lst.append(int(a+b+c))
    lst.append(int(a+c+b))
    lst.append(int(b+a+c))
    lst.append(int(b+c+a))
    lst.append(int(c+a+b))
    lst.append(int(c+b+a))
    for x in lst:
        if x < 100:
            lst.remove(x)
    for y in lst:
        print(y,end=' ')
if b == a+3 and b>0 and a>0:
    m = []
    for x in range(a,b):
        m.append(str(x))
    zuhe(m)
else:
    print('illegal input')
