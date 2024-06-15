nums = eval(input())
kong = []
kong2 = []
for i in nums:
    if nums.count(i)>=2:
        pass
    else:
        kong.append(i)
if len(kong) == 0:
    print(False)
else:
    kong.sort()
    for y in kong:
        g = str(y)
        kong2.append(g)
    print(",".join(kong2))
