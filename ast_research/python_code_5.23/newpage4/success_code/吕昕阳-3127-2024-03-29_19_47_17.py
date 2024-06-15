n=int(input())
lst=[]
for i in range(1,n+1):
    lst.append(i)
def demo(lst,n):
    return (lst[n:]+lst[:n])
print(demo(lst[:],1))

