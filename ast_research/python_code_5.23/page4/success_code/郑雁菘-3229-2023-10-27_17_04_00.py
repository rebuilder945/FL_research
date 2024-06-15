A = eval(input())
B = []
C = []
for i in A:
    X = A.count(i)
    C.append(X)
    if X == 1:
        B.append(i)
if min(C) > 2:
    print("False")
else:
    B.sort(reverse=False)
    B = [str(i) for i in B]
    M = (",".join(B))
    print(M)
    


   

                


