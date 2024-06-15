a=eval(input())
q=[]
for i in a:
    if i==0:
        t=i
        a.remove(0)
        q.append(t)
    else:
        continue
a.extend(q)
print(a)        

