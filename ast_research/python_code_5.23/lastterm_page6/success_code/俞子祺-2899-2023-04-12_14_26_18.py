n,m=map(int,input().split(" "))
for i in range(n,m):
    for x in range(n,m):
        for y in range(n,m):
            if i!=x and x!=y and y!=i:
                print(str(i)+str(x)+str(y))
else:
    print("illegal input")


