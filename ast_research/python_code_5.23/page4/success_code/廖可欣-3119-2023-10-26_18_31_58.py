nums = eval(input())
kong = []
nums.reverse()
for i in nums:
    if i in kong:
        pass
    else:
        kong.append(i)
print(kong)
