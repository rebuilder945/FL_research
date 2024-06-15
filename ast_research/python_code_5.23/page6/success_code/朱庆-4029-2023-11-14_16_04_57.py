n,m = map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    shu = x*100+y*10+z
                    if shu>99:
                        print(shu,end=' ')
else:
    print("illegl input")
