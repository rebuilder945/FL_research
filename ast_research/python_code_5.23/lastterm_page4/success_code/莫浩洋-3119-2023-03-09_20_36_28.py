#删除不要与遍历操作同时进行，否则会导致混乱

"""for i in a:
    b=a.count(i)
    if b==1:
        continue
    else :
        for x in range(0,b-1):
            a.remove(i)
以上为错误操作警惕
"""
list1 = list(eval(input()))
list1.reverse()                        #将list1翻转
list2 = ['']
for i in list1:
    if i not in list2:
        list2.insert(0, i)             #向list2的首位加入i
list2.pop()                            #去掉末尾的  ''
print(list2)

