A=eval(input())
B=[]
for i in range(len(A)):
    if A[i:].count(A[i])==1:
        B.append(A[i])
print(B)


