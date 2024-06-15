a=int(input())
b=[]
for i in range(0,a+1):
    b.append(i)
def demo(l,n):
    return(l[n:]+l[:n])
print(demo(b[:],1))
