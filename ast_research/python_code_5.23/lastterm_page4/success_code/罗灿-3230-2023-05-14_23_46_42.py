nums=eval(input())
nums.sort(reverse=True)
numstr="".join(str(x) for x in nums)
print(numstr)
