def ss(i):
    for x in range(2,i//2+1):
        if i%x==0:
            return False
    return True
def hws(i):
    n = str(i)
    m = n[::-1]
    if n==m:
        return n
i = eval(input())
if (i-int(i)>0) or int(i)<0:
    print("illegal input")
else:
    i = int(i)
    l = []
    for a in range (2,i):
        if ss(a) and hws(a):
            l.append(a)
    for b in range(len(l)):
        print(l[b],end="")
