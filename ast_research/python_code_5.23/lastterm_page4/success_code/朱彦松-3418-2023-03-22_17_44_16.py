def maxsum(arr):
    n = len(arr) // 2
    arr.sort()
    ans = 0
    for i in range(n):
        ans += arr[i * 2]  # 取相邻两个数的最小值相加
    return ans





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

