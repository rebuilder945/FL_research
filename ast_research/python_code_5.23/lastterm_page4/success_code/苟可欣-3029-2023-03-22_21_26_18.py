a=list(input())
b=eval(input())
lens=len(a)
for x in range(lens):
    c=a[x]
    d=b[x]
    c.append([c+","+d])
print(c)
