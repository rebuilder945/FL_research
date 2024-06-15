A = input().split(",")
n,m = eval(input())
x = A[n]
if n > int(len(A))-1:
    print("error")
for i in range(m):
    A.append(x)
    A = [int(i) for i in A]
print(A)
