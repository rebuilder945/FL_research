lst = eval(input())
lst1 = lst.copy()
for i in lst:
    if i==0:
        lst1.remove(i)
        lst1.append(0)#将数值为0的元素加到列表尾部
print(lst1)
      
