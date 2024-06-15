from collections import Counter
def find_unique(nums):
    counter = Counter(nums)
    unique_nums = [num for num in nums if counter[num] == 1]
    if unique_nums:
        unique_nums.sort()
        return','.join(map(str,unique_nums)) 
    else:
        return False

lst=eval(input())
lst2=find_unique(lst)

print(lst2)
