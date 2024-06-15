n,m  = map(int,input.split())
if (n>=m) or (m>9) or (n<0) or (m-n<=3):
    print("illegal input")
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and z!=x:
                    N = x*100+y*10+z
                    if N>99:
                        print(N,end =" ")
