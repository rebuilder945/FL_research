lst=eval(input())
a=max(lst)
b=min(lst)
new=[]
for x in lst:
    if (x!=a and x!=b):
        new.append(x)
print(new)
