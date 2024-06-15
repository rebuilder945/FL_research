A = eval(input())
n, m = map(int, input().split(','))
if n < 0 or m >= len(A) or n>m:
    print("error")
else:
    del A[n:m]
    print(A)
