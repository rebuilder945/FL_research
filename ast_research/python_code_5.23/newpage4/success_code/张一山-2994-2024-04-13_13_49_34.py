M=list(eval(input()))
n,m=eval(input())
s=0
L=len(M)
if n>L:
    print("error")
else:
    while s<m:
        M.append(M[n])
        s+=1
    print(M)

