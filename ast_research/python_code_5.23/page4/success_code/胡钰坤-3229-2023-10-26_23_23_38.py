nums = eval(input())
ls = []
for i in nums:
    if nums.count(i) == 1:
        ls.append(i)
if len(ls) > 0:
    ls.sort()
    ls = ','.join(str(i) for i in ls)
    print(ls)
else:
    print("False")

