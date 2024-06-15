A = input().split(",")
n,m = eval(input())
if n > 0 and n > int(len(A))-1:
    print("error")
elif n < 0 and n < -int(len(A)):
    print("eeror")
else:
    X = A[n]
    for i in range(m):
        A.append(X)
    A = [int(i) for i in A]
    print(A)
