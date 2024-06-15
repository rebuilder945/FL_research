
def find_once(nums): #定义函数
    count = {} #创建一个空字典
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    once_nums = [num for num, freq in count.items() if freq == 1]
    if once_nums:
        return ','.join(sorted(once_nums))
    else:
        return 'False'
nums = input().strip('[]').split(',')
print(find_once(nums))
