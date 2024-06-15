n,m=map(int,input().split())
for i in range(n,m):
    for a in range(n,m):
        for c in range(n,m):
            shu=eval(str(i)+str(a)+str(c))
            if m-n!=3 or shu<=100:
                print("illegal input")
            else:
                print(shu,end=" ")
