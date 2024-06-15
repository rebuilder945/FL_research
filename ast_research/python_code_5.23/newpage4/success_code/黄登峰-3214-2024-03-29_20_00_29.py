a=eval(input())
n=[]
for i in a:
    if i==0:
        a.remove(i)
        n.append(0)
    else:
        continue
a.extend(n)
print(a) 
