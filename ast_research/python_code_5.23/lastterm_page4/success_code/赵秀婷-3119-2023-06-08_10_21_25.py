# 删除列表中的重复值        (不同元素在列表中的相对位置不应被改变)
# 删除前k-1个元素，保留最后一个     用remove()

lst=eval(input())
for i in lst:
    if lst.count(i)>1:
        lst.remove(i)
print(lst)
