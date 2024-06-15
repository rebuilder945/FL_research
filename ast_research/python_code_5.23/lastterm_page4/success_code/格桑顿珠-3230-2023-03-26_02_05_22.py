nums = eval(input())
nums.sort(reverse=True)
nums2 = [str(x) for x in nums]
str1 ="".join(nums2)
n = int(str1)
print(str1)

