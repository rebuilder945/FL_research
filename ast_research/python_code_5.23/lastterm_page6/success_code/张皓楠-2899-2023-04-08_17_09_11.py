[n,m] = input().split(" ")
a,b = eval(n),eval(m)
if not a%1 and not b%1 and b>0 and b-a>=3 and a>=0:
    for i in range(a,b+1):
        for j in range(a,b+1):
            for k in range(a,b+1):
                if i!=j!=k:
                    c = 100*i + 10*j + k
                    print(c,end = " ")
else:
    print("illegal input")
