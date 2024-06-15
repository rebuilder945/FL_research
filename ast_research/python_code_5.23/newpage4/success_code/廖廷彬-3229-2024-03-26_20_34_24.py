def find_unique_elements(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    unique_elements = [num for num, freq in count.items() if freq == 1]
    
    if unique_elements:
        return ','.join(map(str, sorted(unique_elements)))
    else:
        return "False"

# 读入一个自然数列表
input_str = input("请输入一个包含自然数的列表，数字之间用逗号分隔: ")
num_list = [int(x) for x in input_str.strip('[]').split(',')]

# 调用函数找出只出现一次的元素并输出结果
result = find_unique_elements(num_list)
print(result)

