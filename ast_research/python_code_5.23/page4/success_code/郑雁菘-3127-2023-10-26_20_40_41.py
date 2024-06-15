A = eval(input())
B = []
for i in range(1,A+1):
    B.append(i)
a = B[0]
del B[0]
B.append(a)
print(B)
