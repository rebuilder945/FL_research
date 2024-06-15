def zuhe(list):
    lst = []
    for x in list:
        x1 = list.copy()
        x1.remove(x)
        for y in x1:
            y1 = x1.copy()
            y1.remove(y)
            for z in y1:
                lst.append(int(x+y+z))
    n = []
    for i in lst:
        if i > 100 and i <1000:
            n.append(i)
    if n == None:
        print('illegal input')
    else:
        for h in n:
            print(h,end=' ')

n = [eval(x) for x in input().split()]
a = n[0]
b = n[1]
if b >= a+3 and b>=0 and a>=0 and type(a)==type(b) and type(a)==int:
    m = []
    for j in range(a,b):
        m.append(str(j))
    zuhe(m)
else:
    print('illegal input')
