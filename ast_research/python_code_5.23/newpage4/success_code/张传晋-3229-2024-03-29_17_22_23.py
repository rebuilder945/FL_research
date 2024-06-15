
def find_unique_elements(num_list):
    # 使用字典统计每个元素出现的次数
    count_dict = {}
    for num in num_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # 找出只出现一次的元素
    unique_elements = [num for num, count in count_dict.items() if count == 1]
    
    # 如果没有只出现一次的元素，返回False
    if not unique_elements:
        return False
    
    # 否则，升序输出只出现一次的元素
    unique_elements.sort()
    return unique_elements
num_list = eval(input())
result = find_unique_elements(num_list)
print(result)


