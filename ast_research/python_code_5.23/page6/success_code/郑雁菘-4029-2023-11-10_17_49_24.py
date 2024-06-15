A = input().split()
B = []
n , m = int(A[0]) , int(A[-1])
if n >= m or n < 0 or m < 0 or n >8:
    print("illegal input")
else:
    for i in range(n,m):
        for x in range(n,m):
            for y in range(n,m):
                if i != x and x != y and y != i:
                    sum = str(i) + str(x) + str(y)
                    B.append(sum)
print(" ".join(B))

