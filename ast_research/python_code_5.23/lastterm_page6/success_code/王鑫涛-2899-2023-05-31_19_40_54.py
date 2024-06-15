x,y=input().split(' ')
n,m=eval(x),eval(y)
if not n <m-3:
    print('illegal input')
else:
    M=range(n,m)
    for i in M:
        for q in M:
            for r in M:
                if i!=q and i!=r and q!=r:
                    print(str(i)+str(q)+str(r),end='  ')
