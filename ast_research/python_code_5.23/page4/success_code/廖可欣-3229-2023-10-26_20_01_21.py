nums = eval(input())
kong = []
for i in nums:
    if nums.count(i)>=2:
        pass
    else:
        kong.append(i)
if len(kong) == 0:
    print(False)
else:
    kong.sort()
    print(kong)
