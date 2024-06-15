n,m,l = eval(input())
A = [n]
for i in range(m-1):
    for x in A:
        B = int(x)+l
        A.append(B)
print(n)
