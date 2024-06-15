h = int(input(""))  # 获取用户输入的起始高度
n = int(input("")) # 次数
tour = []
height = []

for i in range(1,n+1): #利用for in 对次数进行循环，次数的循环影响着总体的高度以及里程数
    if i == 1:
        tour.append(h)
    else:
        tour.append(2*h)
    h /=2 #此时的高度等与前一次的高度一般
    height.append(h)
s = sum(tour)
u = height[-1]

print("%%f"%(n,s))

