nums = eval(input())
res = []
for num in nums:
    if nums.count(num) == 1:
       res.append(num)
res.sort()
if res:
    print(",".jion(str(i) for i in res))
else:
    print("False")

