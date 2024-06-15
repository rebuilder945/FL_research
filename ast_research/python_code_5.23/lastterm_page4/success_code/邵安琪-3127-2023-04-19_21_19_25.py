n=eval(input())
lst=[]
for x in [1,n]:
    if x not in lst:
        lst.append(x)
lst.insert(-1,lst.pop())
print(lst)
