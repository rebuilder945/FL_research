#要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。可以用sort排序来判断有没有重复的！
list1 = input().split(",")     #切不可一边遍历列表，一边删除列表中的元素!!!我焯！
list2 = list1                     #list2 = list1.sort()格式不行啊
list2.sort()
for i in range(len(list2)-1):
        if list2[i] == list2[i+1]:
            del list2[i]
print(list2)
