def ling(y):
    x=y.count(0)
    while 0 in y:
        y.remove(0)
    for i in range(x):
        y.append(0)
    return(y)
a=eval(input())
ling(a)
print(a)
