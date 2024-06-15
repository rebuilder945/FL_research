A = list(map(float,input().split(",")))
B = list(map(float,input().split(",")))
import math
dis1 = abs(A[0]-B[0])
dis2 = abs(A[1]-B[1])
dis3 = math.sqrt(dis1**2+dis2**2)
print("%.2f"%dis3)
