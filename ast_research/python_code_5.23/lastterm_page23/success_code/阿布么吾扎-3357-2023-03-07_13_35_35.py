d = eval(input('飞机名称:'))
a = eval(input('加速度:'))
v = eval(input('起飞速度:'))
length = v*v/(2*a)
print('The acceleration of',d,'is',a,'M/s,the take-off speed is',v,'M/s,and the shortest take-off runaway length is',length,'M.')

