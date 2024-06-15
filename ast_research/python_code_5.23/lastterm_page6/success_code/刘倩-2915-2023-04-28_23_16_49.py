num = input()
nums = [int(x) for x in num]
a = nums[0]
b = nums[1]
c = nums[2]
if int(num) == a**3+b**3+c**3:
    print(num)
else:
    print("none")
