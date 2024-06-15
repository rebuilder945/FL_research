M=list(eval(input()))
n,m=eval(input())
s=0
L=len(M)
if n>L:
    print("error")

elif 0 < n <= L:
    while s<m:
         M.append(M[n])
         s+=1
    print(M)
else:
    n1=len(M)+n
    while s<m:
         M.append(M[n1])
         s+=1
    print(M)
