L=eval(input())
b=0
for i in range(len(L)):
    if L[i] != 0:
        L[b]=L[i]
        b=b+1
for j in range(b,len(L)):
    L[j]=0
print(L)

