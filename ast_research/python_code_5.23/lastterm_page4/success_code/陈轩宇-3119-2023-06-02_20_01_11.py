a = eval(input())
for i in a:
    jishu = a.count(i)
    if jishu>1:
        while jishu>1:
            a.remove(i)
            jishu-=1
print(a)

    
