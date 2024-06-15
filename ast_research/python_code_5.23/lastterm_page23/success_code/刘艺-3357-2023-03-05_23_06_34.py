n=input()#飞机的名称
a=eval(input())#加速度
v=eval(input())#起飞速度
L=(v*v)/(2*a)
print('The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M.'%(n,a,v,L))

