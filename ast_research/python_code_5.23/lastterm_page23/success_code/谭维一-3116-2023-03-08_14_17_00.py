x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
import math
dis1 = abs(x1-x2)
dis2 = abs(y1-y2)
dis3 = math.sqrt(dis1**2+dis2**2)
print("%.2f"%dis3)
