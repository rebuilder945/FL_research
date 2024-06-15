A = eval(input())
B = []
for i in A:
    X = A.count(i)
    if X > i:
        print("False")
for i in A:
    X = A.count(i)
    if X == 1:
        B.append(i)
B.sort(reverse=False)
B = [str(i) for i in B]
M = (",".join(B))
print(M)


   

                


