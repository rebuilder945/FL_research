list1=eval(input())
list2=list1.copy()
for x1 in list1:
    jishu=list2.count(x1)
    if jishu>1:
        while jishu>1:
            list2.remove(x1)
            jishu-=1
print(list2)

