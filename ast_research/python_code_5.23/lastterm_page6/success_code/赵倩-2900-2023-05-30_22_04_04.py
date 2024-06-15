def s(i):
    for x in range(2,i):
        if i%x==0:
            return 1
    return 0
def h(i):
    l=str(i)
    if l==l[::-1]:
        return 0
a=eval(input())
if a!=int(a) and a<0:
    print("illegal input")
else:
    b=[]
    for i in range(2,a):
        if s(i)==0 and h(i)==0:
            b.append(i)
    print(b)


