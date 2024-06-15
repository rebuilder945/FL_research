a = input()
i = 0
nums = []
while i>=0:
    if a!="#":
        i = i + 1
        nums.append(int(a))
        a = input()
    else:
        break
print(i,sum(nums))

