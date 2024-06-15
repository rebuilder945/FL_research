def findss(a):
    for x in range(2,a):
        if a%x==0:
            return False
    return True
def findhws(a):
    a=str(a)
    b=[a[x] for x in range(len(a))]
    c=[b[-x] for x in range(1,len(a)+1)]
    if c==b:
        return True
    else:
        return False
u=eval(input())
q=[]
if u%1!=0 or u<1:
    print('illegal input')
else:
    for x in range(2,u):
        if findss(x) and findhws(x):
            q.append(x)
print(' '.join(str(x) for x in q))



