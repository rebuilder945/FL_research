n=eval(input())
lst=[]
for x in range(1,n+1):
    if x not in lst:
        lst.append(x)
m=lst[0]
lst.pop(0)
lst.append(m)
print(lst)
