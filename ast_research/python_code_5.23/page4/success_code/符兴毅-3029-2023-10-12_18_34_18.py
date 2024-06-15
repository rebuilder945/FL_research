name = input().split(',')
# print(name)
nums = eval(input())
aim = []
for i in range(len(name)):
    port = []
    port.append(name[i])
    port.append(nums[i])
    aim.append(port)
print(aim)

