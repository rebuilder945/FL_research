m=eval(input())
n=[]
for i in range(len(m)):
    if m[i:].count(m[i])==1:
       n.append(i)
    else:
        pass
print(n)
