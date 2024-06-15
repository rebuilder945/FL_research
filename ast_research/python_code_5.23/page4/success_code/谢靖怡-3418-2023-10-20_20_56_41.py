l = [1, 2, 3, 4]
random.shuffle(l)
min_l = 0
max_l = 0
for i in range(0, len(l), 2):
      print(l[i], l[i + 1])
      min_l = min_l + min(l[i] + l[i + 1])
      max_l = max_l + max(l[i] + l[i + 1])
print("最小值：", min_l)
print("最大值:   ", max_l)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

