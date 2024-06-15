def largest_number(digits):
    # 将列表中的每个数字转换为字符串
    digits = list(map(str, digits))
    # 对字符串进行排序，相同的数字字典顺序排在前（Python中是升序）
    # 因此需要降序排列，可以通过反转列表或者使用sorted函数的reverse参数
    digits.sort(reverse=True)
    # 将排序后的字符串连接起来形成一个整数
    largest_num = ''.join(digits)
    return largest_num

# 读取输入
input_digits = input()
# 验证输入是否只包含数字
if input_digits.isdigit():
    # 计算并输出最大的整数
    print(largest_number(list(input_digits)))
else:
    print("输入错误：请输入一个只包含数字的列表。")

