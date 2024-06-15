A = eval(input())
B = []
for x in range(int(len(A))):
    for i in A:
        m = max(A)
        B.append(m)
        A.remove(m)
B = [str(i) for i in B]
X = int("".join(B))
print(X)
    
