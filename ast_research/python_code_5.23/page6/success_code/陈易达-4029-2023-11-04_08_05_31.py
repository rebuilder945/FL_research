n,m = map(int,input().split())
if m-n < 3 or m>10 or n<0:
    print('illegal input')
else:
    ls = []
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z and x!=0:
                    ls.append(str(x)+str(y)+str(z))
    result = " ".join(map(str,ls))
    print(result)
