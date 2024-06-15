def shift(lst):
    last = lst.pop()  # 取出最后一个元素
    lst.insert(0, last)  # 将最后一个元素插入到列表最前面

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

