n=int(input())
l=[]
for i in range(n):
    l.append(i)
l2=[]
if i==l[-1]:
    l2[-1]=l[0]
else:
    l2[i]=l[i+1]
print(l2)
