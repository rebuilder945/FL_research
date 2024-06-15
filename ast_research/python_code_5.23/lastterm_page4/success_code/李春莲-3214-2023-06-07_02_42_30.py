l=eval(input())
l2=[]
for i in l:
    if i==0:
        l.remove(i)
        l2.append(i)
print(l+l2)
