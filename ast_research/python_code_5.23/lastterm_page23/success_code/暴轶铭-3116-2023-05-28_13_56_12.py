import math
a = map(float, input().split(","))
b = map(float, input().split(","))
distance = math.dist([a],[b])
print("%.2f"%(distance))
