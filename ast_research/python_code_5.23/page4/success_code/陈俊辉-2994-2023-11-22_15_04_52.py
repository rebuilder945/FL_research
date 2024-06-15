a=map(int,input().split(','))
n,m=map(int,input().split(','))
a=list(a)
b=[]
if n-1>=len(a):
    print("error")
elif n-1<len(a):
  while m>0:
    b.append(a[n])
    m-=1
    for i in range(len(b)):
        a.append(b[i])
print(a)

