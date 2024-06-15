#删除列表中的最大元素和最小元素
lst=eval(input())
x=max(lst)
y=min(lst)
while x in lst:
    lst.remove(x)
while y in lst:
    lst.remove(y)
print(lst)
