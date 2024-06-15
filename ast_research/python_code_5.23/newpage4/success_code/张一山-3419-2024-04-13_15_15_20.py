def calDegrees(N):
    M=[]
    for x in N:
        M.append(N.count(x))
    M.sort()
    return M[-1]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

