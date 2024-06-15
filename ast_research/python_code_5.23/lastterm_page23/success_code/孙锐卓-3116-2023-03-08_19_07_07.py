import math
Ax,Ay = eval(input())
Bx,By = eval(input())
L = math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By))
print('%.2f'%L)
