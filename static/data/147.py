nums = eval(input())
zero_count = nums.count(0)
#变量名不能包含连字符（-），所以不能被赋值，应使用下划线（_）代替。

while nums.count(0) > 0:
    nums.remove(0)

zeros = [0] * zero_count

nums += zeros
print(nums)