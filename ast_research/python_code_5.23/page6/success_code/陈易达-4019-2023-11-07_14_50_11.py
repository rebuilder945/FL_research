nums = ""
num = input()
for x in num:
    nums += str((int(x)+5)%10)
nums = nums[::-1]
print(nums)
