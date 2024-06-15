[n,m] = input().split(" ")
a,b = eval(n),eval(m)
d = True
for i in range(a,b):
    for j in range(a,b):
        for k in range(a,b):
            if i!=j!=k!=i:
                c = 100*i + 10*j + k
                if c>100 and c<1000:
                    print(c,end = " ")
                    d = False
if d:
    print("illegal input")
