n=eval(input())
a=min(n)
b=max(n)
lst=[]
for x in n:
    if x != a and x !=b:
        lst.append(x)
print(lst)
