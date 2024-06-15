lst=[]
for i in range(100000):
    a=eval(input())
    if a=="#":
        break
    else:
        lst.append(a)
n=len(lst)
m=sum(lst)
print(n,m)

