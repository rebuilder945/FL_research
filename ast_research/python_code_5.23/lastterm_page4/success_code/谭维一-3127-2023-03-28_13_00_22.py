x = int(input())
ls = []
for i in range(1,x+1):
    ls.append(i)
def demo(m,n):
    return (m[n:]+m[:n])  
print(demo(ls[:],1))
