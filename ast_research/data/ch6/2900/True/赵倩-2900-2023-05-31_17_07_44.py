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
if a>1 and type(a)==int:
    b=[]
    for i in range(2,a):
        if s(i)==0 and h(i)==0:
            b.append(i)
    print(" ".join(str(y)for y in b))
else: 
    print("illegal input")


