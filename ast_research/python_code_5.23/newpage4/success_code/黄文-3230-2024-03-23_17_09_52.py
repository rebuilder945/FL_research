# 读取用户输入
input_str = input("")

# 将输入的字符串转换为列表
# 注意：这里使用strip()去掉两端的空格，split()以逗号分隔每个数字
numbers = input_str.strip('[]').split(',')

# 将列表中的字符串转换为整数
lst = list(map(int, numbers))

# 确保列表中有数字
if not lst:
    print("")
else:
    # 对列表中的数字进行排序
    lst.sort(reverse=True)
    
    # 将排序后的数字连接成一个整数
    max_number = int(''.join(map(str, lst)))
    
    # 输出最大整数
    print(max_number)

