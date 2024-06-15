def max_num(digits):
    sorted_digits = sorted(digits,reverse=True)
    max_num_str = ''.join(str(digit)for digit in sorted_digits)
    return int(max_num_str)
input_str = input("请输入一组数字，每个数字之前用逗号分隔：")
input_list = [int(digit.strip()) for digit in input_str.split(',')]
print("组成的最大整数是：", max_num(input_list))

