a=input()
c=[]
for i in range(len(a)):
    c.append(int(a[i]))
for j in c:
    j=(j+5)%10
c.reverse()
for k in c:
    print(k,end="")
