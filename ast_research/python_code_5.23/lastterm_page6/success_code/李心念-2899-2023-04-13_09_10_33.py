n = [eval(x) for x in input().split()]
a = n[0]
b = n[1]
def zuhe(list):
    lst = []
    for x in list:
        x1 = list.remove(x)
        for y in x1:
            y1 = list.remove(y)
            for z in y1:
                lst.append(x+y+z)
    for x in lst:
        if x < 100:
            lst.remove(x)
    for y in lst:
        print(y,end=' ')
if b > a+3 and b>0 and a>0:
    m = []
    for x in range(a,b):
        m.append(str(x))
    zuhe(m)
else:
    print('illegal input')
