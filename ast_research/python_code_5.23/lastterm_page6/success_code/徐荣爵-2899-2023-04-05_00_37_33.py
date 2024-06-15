n,m = map(int,input().split())
if n >= 0 and m <= 10 and m - n > 2:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i != j and i != k and j != k:
                    num = 100*i + 10*j + k 
                    if num > 100:
                        print(num,end=' ')
else:
    print('illegal input')
