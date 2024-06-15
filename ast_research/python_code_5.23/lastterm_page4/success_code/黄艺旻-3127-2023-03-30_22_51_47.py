x = int(input())
ls = []
for i in range(1,x+1):
    ls.append(i)
def demo(l,n):
    return (l[n:]+l[:n]) 
print(demo(ls[:],1))

