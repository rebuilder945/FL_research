n,m = input().split(" ")
if n.isdigit() == True and m.isdigit() == True and 0<=int(n)<int(m)<=9:
    #上面判断输入的数是0到9的整数
    n,m = int(n),int(m)
    num = [i for i in range(n,m)]
    #从n到m的数生成一个表格
    output = []
    for j in num:
        for k in num:
            for l in num:
                if k != l and k != j and l != j:
                    output.append(str(j)+str(k)+str(l))
    for o in output:
        if str(o).startswith("0") is True:
            output.remove(o)
        else:
            print(o,end=" ")
else:
    print("illegal input")
