def find_unique(lst):
    count_dict = {}  # 用字典记录每个数字出现的次数
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    unique_nums = []  # 存储只出现一次的数字
    for num, count in count_dict.items():
        if count == 1:
            unique_nums.append(num)
    
    if len(unique_nums) == 0:  # 没有只出现一次的数字，返回False
        return False
    
    sorted_nums = sorted(unique_nums)  # 升序排序
    return ','.join(str(num) for num in sorted_nums)  # 转换为字符串输出，每个数字之间用逗号分隔
lst=eval(input())
print(find_unique(lst))

