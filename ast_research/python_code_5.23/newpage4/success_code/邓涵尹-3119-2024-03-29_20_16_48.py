#def find_once(nums): #定义函数
#   count = {} #创建一个空字典
#   for num in count:
#       if num in count:
#           del nums[num]
#        else:
#            continue
#    once_nums = [num for num, freq in count.items() if freq == 1]
#    if once_nums:
#        return ','.join(sorted(once_nums))
#nums = input().strip('[]').split(',')
#print(find_once(nums))

#nums = eval(input())
#def find_same(nums):
#   for num in nums:
#        if num 


def find_same(nums):
    c = []
    for num in nums:
        if nums.count(num) > 1:
            # 保留最后一个重复元素
            if num not in c:
                c.append(num)
        else:
            c.append(num)
    return c

nums = eval(input())
print(find_same(nums))
