n,m = map(int,input().split())
if m - n >= 3 and 0 < n < m < 11:
#用for循环嵌套实现全排列
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x != y and y != z and x != z :
                    N = x*100 + y*10 + z
                    if N > 99:
                        print(N,end=" ")
else:
    print("illegal input")                    




