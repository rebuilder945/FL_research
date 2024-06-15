def find_majority_element(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] +=1
        else:
            counts[num] = 1
n = len(nums)
for num,count in counts.item():
    if count > n//2:
        print(num)
print('False')





nums = eval(input())
y = search(nums)
print(y)


