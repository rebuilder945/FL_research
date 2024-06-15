a = sorted(nums)
b = []
for i in range(0,len(a),2):
    b.append(a[i])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

