lst=eval(input())
lst1=lst.copy()
for x in lst:
    if lst1.count(x)>1:#count函数可以计算出这个x重复的个数
        lst1.remove(x)#可以删除列表中某个值的第一个匹配项
print(lst1)
