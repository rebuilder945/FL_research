n=eval(input())
lst=[]
for x in range(1,n+1):
    if x not in lst:
        lst.append(x)
lst.insert(-1,lst.pop(0))
print(lst)
