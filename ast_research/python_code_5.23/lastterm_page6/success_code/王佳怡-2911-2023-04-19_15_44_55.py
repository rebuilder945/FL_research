a=input()
c=[]
for i in range(len(a)):
    c.append(int(a[i]))
for j in c:
    c=(c+5)%10
c.reverse
for k in c:
    print(c,end="")
