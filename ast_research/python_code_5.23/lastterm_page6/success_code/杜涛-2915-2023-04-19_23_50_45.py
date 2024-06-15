def f1(x):
    a=list(str(x))
    b=0
    for i in a:
        b+=int(i)**len(a)
    return b
def f(x):
    lst=[]
    for i in range(100,x+1):
        if f1(i)==i:
            lst.append(i)
    if lst==[]:
        return 1
    else:
        return lst
x=eval(input())
a=f(x)
if a!=1:
    for i in a:
        print(i)
else:
    print("none")

