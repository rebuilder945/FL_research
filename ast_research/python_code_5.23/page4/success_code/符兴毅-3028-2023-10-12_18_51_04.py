start, nums, next = eval(input())
n = 1
aim = []
aim.append(start)
while n < nums:
    start += next
    aim.append(start)
    n += 1
print(aim)

