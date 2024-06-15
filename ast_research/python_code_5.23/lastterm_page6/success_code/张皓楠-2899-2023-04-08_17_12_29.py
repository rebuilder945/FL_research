[n,m] = input().split(" ")
a,b = eval(n),eval(m)
if not a%1 and not b%1 and b>0 and b-a>=3 and a>=0:
    for i in range(a,b):
        for j in range(a,b):
            for k in range(a,b):
                if i!=j!=k!=i:
                    c = 100*i + 10*j + k
                    if c>100 and c<1000:
                        print(c,end = " ")
else:
    print("illegal input")
