def calDegrees(x):
    room=[]
    for i in range(len(x)):
        s=x.count(x[i])
        room.append(s)
        return max(room)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

