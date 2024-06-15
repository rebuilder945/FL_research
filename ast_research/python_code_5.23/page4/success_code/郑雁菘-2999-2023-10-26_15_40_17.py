A = input().split()
M = input().split()
n = int(M[0])
m = int(M[-1])
X = A[n]
Y = A[m]
if n > 0 and m > 0:
    del A[n]
    del A[m-1]
    A.insert(n,Y)
    A.insert(m,X)
    print(A)
elif n < 0 and m > 0:
    if int(len(A)+n) == m:
        print(A)
    else:
        n = len(A)+n + 1
        del A[n]
        del A[m-1]
        A.insert(n,Y)
        A.insert(m,X)
        print(A)
elif n > 0 and m < 0:
    if int(len(A)+n) == m:
        print(A)
    else:
        m = len(A)+ m + 1
        del A[n]
        del A[m-1]
        A.insert(n,Y)
        A.insert(m,X)
        print(A)
else:
    del A[n]
    del A[m-1]
    A.insert(n,Y)
    A.insert(m,X)
    print(A)


    

