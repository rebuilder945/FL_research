n = eval(input())
numbers = [x for x in range(1, n + 1)]  # 注意逗号的使用
# #试图创建一个范围为1到输入数字n的列表，但是在列表推导式中的语法有误，应该使用逗号而不是点来分隔范围的开始和结束。
for i in range(1):
    num = numbers.pop(0)
    numbers.append(num)
    print(numbers)