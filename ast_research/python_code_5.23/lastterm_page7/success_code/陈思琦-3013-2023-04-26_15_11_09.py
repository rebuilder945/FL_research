a,b=eval(input())
GDP={}
for x,y in a,b:
    GDP[x]=GDP.get(x,y)
b=[]
c=[]
for i in GDP:
    b.append(i)
for q in GDP.values():
    b.append(q)
if 'India'in GDP:
    print('yes')
else:
    print('no')
print(sum(c))
