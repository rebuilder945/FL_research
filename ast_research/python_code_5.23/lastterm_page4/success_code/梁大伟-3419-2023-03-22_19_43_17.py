def calDegrees(x):
    room=[]
    for i in range(len(x)):
        a=x.count(x[i])
        room.append(a)
    return max(room)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

