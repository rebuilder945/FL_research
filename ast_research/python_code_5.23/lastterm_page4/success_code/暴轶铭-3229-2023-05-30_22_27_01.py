#输入一个自然数列表，找出只出现一次的元素，并升序输出。如果没有只出现一次的元素，则输出False。
nums = eval(input())
result = []
for i in nums:
    if nums.count(i) == 1:
        result.append(i)
    else:
        pass
if len(result) == 0:
    print("False")
else:
    result.sort(reverse = False)
    result = [str(i) for i in result]
    nums = ",".join(result)
    print(nums)
