#要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。可以用sort排序来判断有没有重复的！
list1 = eval(input())        #切不可一边遍历列表，一边删除列表中的元素!!!我焯！
list2 =list1.copy()                 #copy函数！！这样改变list2时不会变list1  #list2 = list1.sort()格式不行啊
for x in list2:
    times=list1.count(x)
    if times >= 2:
        table.remove(x)
print(list2)  
