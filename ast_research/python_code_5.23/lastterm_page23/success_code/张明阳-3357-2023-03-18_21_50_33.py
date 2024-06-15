sname=input('飞机的名称:')
a=eval(input('加速度:(输入格式为M/s*2)'))
v=eval(input('起飞速度:(输入格式为M/s)'))
lengh=v*v/(2*a)
print('The acceleration of',sname, 's', a,'M / s, the take-off speed is' ,v,'M / s, and the shortest take-off runway length is%.2f'%lengh,'M')


