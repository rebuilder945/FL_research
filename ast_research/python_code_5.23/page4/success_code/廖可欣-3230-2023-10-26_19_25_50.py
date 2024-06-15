nums = eval(input())
kong = []
nums.sort(reverse = True)
for i in nums:
    x = str(i)
    kong.append(x)
print("".join(kong))
