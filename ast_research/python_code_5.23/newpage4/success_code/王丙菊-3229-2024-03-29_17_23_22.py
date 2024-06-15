nums = eval(input())
res = []
for x in nums:
    if nums.count(x) == 1:
       res.append(x)
res.sort()
if res:
    print(",".jion(str(i) for i in res))
else:
    print("False")

