a=input()
c=[]
d=[]
for i in range(len(a)):
    c.append(int(a[i]))
for j in c:
    j=(j+5)%10
    d.append(j)
d.reverse()
for k in d:
    print(k,end="")
