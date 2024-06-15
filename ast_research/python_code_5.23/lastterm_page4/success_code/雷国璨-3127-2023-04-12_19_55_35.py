a=int(input())
b=[]
for i in range(1,a+1):
    b.append(i)
def demo(l,n):
    return(l[n:]+l[:n])
print(demo(b[:],1))
