n=eval(input())
ls=[x for x in range(1,n+1)]
for i in range(len(ls)-1):
    ls[i],ls[i+1]=ls[i+1],ls[i]
print(ls)
