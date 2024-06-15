l=eval(input())
a=max(l)
b=min(l)
l2=[]
for i in l:
    if i==a or i==b:
        l2.remove(i)
print(l2)
