n,m = input().split(" ")
m = int(m)
n = int(n)
if n >= m or m-n < 3:
    print("illeagl input")
else:
    for i in range(n, m):
        for j in range(n, m):
            for k in range(n, m):
                if i != j and j != k and i != k:
                    print(i*100+j*10+k, end=" ")
