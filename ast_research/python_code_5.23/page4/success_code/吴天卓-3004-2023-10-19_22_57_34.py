A=eval(input())
B=[]
C=[]
for i in range(len(A)):
    for x in range(2,A[i]):
        C.append(A[i]%x)
    if 0 in C:
        C.clear()
    else:
        B.append(A[i])
print(B)
