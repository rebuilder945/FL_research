m=input().split(',')
n=input().split(',')
n=[int(x) for x in n]
c={}
for i in range(len(m)):
    c[m[i]]=c.get(m[i],n[i])


g = sorted(c.items(), key = lambda c:c[1])
k=[]
for x in g:
    k.append(list(x))
  
print(k)



