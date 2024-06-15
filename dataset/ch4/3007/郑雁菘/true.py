A = eval(input())
n,m = eval(input())
c = n
if n > m:
    n = m
    m = c
if m < len(A) and n < len(A):
    del A[n:m]
    print(A)
else:
    print("error")
    
    
