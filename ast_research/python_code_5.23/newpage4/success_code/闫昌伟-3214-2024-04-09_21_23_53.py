A=eval(input())
B=[]
C= A.count(0)
for i in range(len(A)):
    if A[i]!=0:
       B.append(A[i])
B.extend([0]*C)
print(B)



