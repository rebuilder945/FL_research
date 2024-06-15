a=input()
b=[]
for i in range(len(a)):
    k=int(a[i])
    k=(k+5)%10
    b.append(k)
for i in range(len(b)//2):
    d=b[i]
    b[i]=b[-i-1]
    b[-i-1]=d
for i in range(len(b)):
    print(b[i],end="")

