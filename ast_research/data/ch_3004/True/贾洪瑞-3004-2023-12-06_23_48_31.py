A=eval(input())
B=[]
C=[]    
for i in range(len(A)): 
    if A[i]!=0 and A[i]!=1:
        for x in range(2,A[i]):
            C.append(A[i]%x)
        if 0 in C:
            C.clear()
        else:
            B.append(A[i])
    else:
        i+=1    
print(B)


