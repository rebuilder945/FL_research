list1=eval(input())
list1.reverse()
list2=list(set(list1))
list2.sort(key=list1.index)
list2.reverse()
print(list2)


# list=eval(input())
# a=set(list)#set的元素顺序1，2,3,4，。。。。
# print(a)

