input_str = input("请输入一个整数列表，包括方括号，元素逗号分隔：")
num_list = input_str.strip('[]').split(',')
num_list = [int(num) for num in num_list]
average = sum(num_list) / len(num_list)
print('{:.2f}'.format(average))

