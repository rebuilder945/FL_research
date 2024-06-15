A = input().split(",")
n,m = eval(input())
x = A[n]
if n > 0 and n > int(len(A))-1:
    print("error")
elif n < 0 and n < -int(len(A)):
    print("eeror")
for i in range(m):
    A.append(x)
    A = [int(i) for i in A]
print(A)
