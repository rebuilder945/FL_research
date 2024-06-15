A=int(input())
B=list(range(1,A+1))
C=B[0]
for i in range(A-1):
    B[i]=B[i+1]
B[-1]=C
print(B)
