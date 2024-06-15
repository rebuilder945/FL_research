n=eval(input())
lst=[]
for x in range(n):
    if x not in lst:
        lst.append(x)
lst.insert(-1,lst.pop())
print(lst)
