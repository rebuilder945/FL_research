a=list(eval(input()))
b=eval(input())
lens=len(a)
k=[]
for x in range(lens):
    c=a[x]
    d=b[x]
    k.append([c+","+"d"])
print(k)
