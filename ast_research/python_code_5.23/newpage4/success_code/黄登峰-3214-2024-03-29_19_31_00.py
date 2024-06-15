a=eval(input())
n=[]
for i in a:
    if i==0:
        n.append(0)
        a.remove(i)
    else:
        continue
a.extend(n)
print(a) 
