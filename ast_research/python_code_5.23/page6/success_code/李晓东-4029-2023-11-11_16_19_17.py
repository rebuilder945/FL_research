n,m = input().split(" ")
n = int(n)
m = int(m)
sums = []
sums1 = []
if m<n or m-n<3 or m<0 or n<0 or n>8:
    print("illegal input")
else:
    for x in range(n,m):
        sums.append(x)
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z and x!=0:
                    s1 = 100*x+10*y+z
                    if s1 not in sums1:
                        sums1.append(s1)
    for a in sums1:
        a = int(a)
        print("%d"%a,end=" ")







