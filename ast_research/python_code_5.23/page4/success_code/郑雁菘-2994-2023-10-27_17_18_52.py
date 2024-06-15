A = input().split(",")
n,m = eval(input())
if n > 0 and n > int(len(A))-1:
    print("error")
elif n < 0 and n < -int(len(A)):
    print("eeror")
else:
    for i in range(m):
        X = A[n]
        A.append(X)
A = [int(i) for i in A]
print(A)
