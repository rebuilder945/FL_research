list1 = eval(input())
list1.reverse()                        #将list1翻转
list2 = ['']
for i in list1:
    if i not in list2:
        list2.insert(0, i)             #向list2的首位加入i
list2.pop()                            #去掉末尾的  ''
print(list2)
