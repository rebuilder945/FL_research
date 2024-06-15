nums = eval(input())
nums.sort(reverse=True)
nums2 = [str(x) for x in nums]
str = "".join(nums2)
n = int(str)
print(n)
