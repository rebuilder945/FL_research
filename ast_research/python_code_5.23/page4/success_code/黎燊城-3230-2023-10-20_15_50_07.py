nums = eval(input())
nums.sort(reverse=True)
a= "".join(str(x) for x in nums)
print(int(a))
