A = eval(input())
B = list(set(A))
B.sort(key=A.index)
print(B)

