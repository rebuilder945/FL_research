a=list(input())
b=input()
lens=len(a)
k=[]
for x in range(lens):
    c=a[x]
    d=b[x]
    k.append([c+","+d])
print(k)
