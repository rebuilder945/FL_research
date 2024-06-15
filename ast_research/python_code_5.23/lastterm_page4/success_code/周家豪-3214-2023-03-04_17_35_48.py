# 读入一个整数列表，把数值为0的元素移动到列表尾部，
# 其他元素的相对顺序不变。输出调整后的列表。

lst1=eval(input())
lst3=lst1.copy()
lst2=[]
for i in lst3:
    if i==0:
        lst2.append(i)
        lst1.remove(i)
lst1.extend(lst2)
print(lst1)

