import math
lst = []
for i in range(2):
    s = list(eval(input()))
    #eval函数后面只能是str
    d = s.split(",")
    lst = lst + s
Ax,Ay,Bx,By = lst
distance = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)
print("{:.2f}".format(distance))
# 对程序来说，你的输入是"10,10"经过split后是["10","10"]
# 你可以直接输入eval(input())
# 他会得到(10,10)


