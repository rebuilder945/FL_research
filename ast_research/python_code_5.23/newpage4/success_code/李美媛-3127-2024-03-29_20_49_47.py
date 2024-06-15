n=int(input())
ls=[i for i in range(1,n+1)]
temp=ls[0]
for i in range(len(ls)-1):
    ls[i]=ls[i+1]
    ls[i+1]=temp
print(ls)
