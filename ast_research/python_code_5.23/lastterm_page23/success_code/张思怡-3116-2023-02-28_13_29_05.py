a,b=eval(input())
c,d=eval(input())
import math
Distance=(a-c)*(a-c)+(b-d)*(b-d)
Distance=math.sqrt(Distance)
print("%.2f"%(Distance))
