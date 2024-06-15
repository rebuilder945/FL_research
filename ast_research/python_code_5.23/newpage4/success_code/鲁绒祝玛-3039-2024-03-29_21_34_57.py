def find_degree(nums):
    counts={}
    for num in nums:
        counts[num]=counts.get(num,0)+1
    degree = max(counts.values())   
    return degree
nums = input()
print(find_degree(nums))
