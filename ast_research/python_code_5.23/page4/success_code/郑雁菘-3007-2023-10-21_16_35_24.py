A = eval(input())
n,m = eval(input())
c = n
if n > m:
    n = m
    m = c
if n > len(A)-1:
    print("error")
else:
    del A[n:m]
    print(A)
    
    
