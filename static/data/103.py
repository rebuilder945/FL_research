def shift(lst):
    lst.insert(0, lst.pop())
#lst.pop() 返回的是被移除的元素，它是一个整数类型（假设列表中的元素都是整数），
#而 insert 方法要求插入一个对象，而不是整数，

input_string = input("请输入一个用逗号分隔的整数列表：")
list1 = [int(x) for x in input_string.split(",")]  # 将输入的字符串转换为整数列表
#可以将 input().split(",") 得到的每个元素转换为整数类型，然后再进行操作。
shift(list1)
print(list1)