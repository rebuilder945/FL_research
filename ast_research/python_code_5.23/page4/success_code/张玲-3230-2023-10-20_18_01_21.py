# 从键盘输入正整数列表
input_list = eval(input().strip())

# 将列表中的数字按位组织成最大整数
max_number = int(''.join(map(str, sorted(input_list, reverse=True))))

# 输出结果
print(max_number)

