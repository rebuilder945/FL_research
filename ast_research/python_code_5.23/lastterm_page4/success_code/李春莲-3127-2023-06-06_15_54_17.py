n=int(input())
l=[]
for i in range(n):
    l.append(i)
print(l)
if i==(-1):
    l[-1]=l[1]
else:
    l[i]=l[i-1]
print(l)
