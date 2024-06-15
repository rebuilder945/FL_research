nums = eval(input())
nums.sort(reverse=True)
nums2 = [str(x) for x in nums]
str1 = "".join(nums2)
a=int(str1)
print(a)


