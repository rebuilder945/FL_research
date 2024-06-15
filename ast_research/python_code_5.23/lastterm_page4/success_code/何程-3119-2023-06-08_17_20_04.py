list1=eval(input())

for x1 in list1:
    jishu=list1.count(x1)
    if jishu>1:
        while jishu>1:
            list1.remove(x1)
            jishu-=1
print(list1)
