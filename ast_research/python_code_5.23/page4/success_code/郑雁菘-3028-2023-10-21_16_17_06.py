n,m,l = eval(input())
A = [n]
for i in range(m-1):
    B = int(A[-1])+l
    A.append(B)
print(A)
