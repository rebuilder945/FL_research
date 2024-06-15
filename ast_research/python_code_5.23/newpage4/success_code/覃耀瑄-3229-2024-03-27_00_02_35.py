def find_unique_elements(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    unique_elements = []
    for num, count in count_dict.items():
        if count == 1:
            unique_elements.append(num)
    
    if unique_elements:
        return ','.join(map(str, sorted(unique_elements)))
    else:
        return False

# 读取输入
input_str = input().strip()
# 去除方括号并按逗号分割转换为整数列表
nums = list(map(int, input_str[1:-1].split(',')))

# 调用函数并输出结果
print(find_unique_elements(nums))

