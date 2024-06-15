# x1, y1 = map(float, input().split(','))
# x2, y2 = map(float, input().split(','))

# f = lambda x: float(x)
# x1, y1 = map(f, input().split(','))
# x2, y2 = map(f, input().split(','))

x1, y1 = [float(i) for i in input().split(',')]
x2, y2 = [float(i) for i in input().split(',')]

import math
print('{:.2f}'.format(math.sqrt(pow((x1 - x2), 2) + \
    pow((y1 - y2), 2))))

