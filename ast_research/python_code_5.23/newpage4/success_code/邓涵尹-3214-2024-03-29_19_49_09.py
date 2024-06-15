#def find_zore(nums):
#    count = {0}
#    for num in nums:
#        if num in count:
#            del nums[num],nums.append('0')
#        else:
#            continue
#nums = input().strip('[]').split(',')
#print("[find_zore(nums)]").split(', ')

#nums = input().strip("[]").split(",")
# 去除列表中的 0，并将其他元素添加到新列表 non_zero_nums 中
#non_zero_nums = [num for num in nums if num!= "0"]
#for num in nums:
#        count={}
#        if num in count == 0:
#            count[num] += 1
#        else:
#            count[num] = 0
#            continue
# 将 0 添加到 non_zero_nums 列表的尾部
#non_zero_nums.append("0"*count(int))
#print(non_zero_nums)

nums = eval(input())
zero_nums = [num for num in nums if num == 0]
other_nums = [num for num in nums if num!= 0]
print(zero_nums + other_nums)
