n,m=map(int,input().split())#输入一行，内容为两个以空格分隔的整数
if 0<=n<m<11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    v=a*100+b*10+c
                    if v >99:
                        print(v,end=" ")#end=''是去除print结果里的换行
else:
    print("illegal input")
