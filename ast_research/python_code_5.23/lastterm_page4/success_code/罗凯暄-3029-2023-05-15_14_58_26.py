name = input().split(',')
nums = eval(input())
result = [[name[i], nums[i]] for i in range(len(name))]
print(result)

