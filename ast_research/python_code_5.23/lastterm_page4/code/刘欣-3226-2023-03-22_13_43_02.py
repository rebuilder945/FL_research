def search(nums):
    num_set = set(nums)
    most_item = False
    for item in num_set:
        if nums.count(item) > len(nums) // 2:
            most_item = item
            return most_item
     return most_item





nums = eval(input())
y = search(nums)
print(y)


