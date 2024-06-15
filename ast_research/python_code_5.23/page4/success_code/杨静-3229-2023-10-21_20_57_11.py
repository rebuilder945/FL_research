nums=eval(input())
list=set(nums)
result=[]
for num in list:
    if nums.count(num) == 1:
            result.append(num)
if len(result) > 0:
        result.sort()
        print(",".join(str(num) for num in result))
else:
    print('False')

