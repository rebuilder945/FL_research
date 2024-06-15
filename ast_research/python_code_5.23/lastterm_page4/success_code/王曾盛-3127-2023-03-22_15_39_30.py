x=int(input())
lst=[]
for i in range(1,x+1):
    lst.append(i)
def demo(l,n):
    return(l[n:]+l[:n])
print(demo(lst[:],1))
