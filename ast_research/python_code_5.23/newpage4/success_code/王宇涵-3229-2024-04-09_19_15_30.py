def find(nums):
    unnums = []
    for num in nums:
        if nums.count(num)==1:
            unnums.append(num)
    if not unnums:
        return False
    unnums.sort()
    return unnums

nums = [int(x) for x in input().spilt()]
result = find(nums)
print(result)

