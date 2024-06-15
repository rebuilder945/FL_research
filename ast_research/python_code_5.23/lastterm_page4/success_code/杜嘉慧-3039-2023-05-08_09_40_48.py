lst = eval(input())
new=[]
a=max(lst)
b=min(lst)
for x in lst:
    if x!=a and x!=b:
        new.append(x)
print(new)
