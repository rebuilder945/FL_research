ls = input().split()
n = eval(ls[0])
m = eval(ls[1])
nums=[]
if (m-n)<3 or m>10 or n>10 or m<0 or n<0:
    print("illegal input")
else:
    ls1=[i for i in range(n,m)]
    for h in ls1:
        for j in ls1:
            for s in ls1:
                if h!=j and j!=s and h!=s and h!=0:
                    nums.append(str(h)+str(j)+str(s))
    print(" ".join(str(x) for x in nums))





