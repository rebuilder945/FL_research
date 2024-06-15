m=eval(input())
n=[]
for i in range(len(m)):
    if m[i:].count(m[i])==1:
      n.append(m[i])
    else:
        pass
print(n)
