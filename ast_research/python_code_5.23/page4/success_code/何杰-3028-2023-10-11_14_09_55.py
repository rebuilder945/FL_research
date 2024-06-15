a,b,c=eval(input())
n=[]
n.append(a)
for i in range(b-1):
    a=a+c
    n.append(a)
print(n)
