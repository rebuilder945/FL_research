def length():
    l = v*v/(2*a)
    return l
name = input()
a = eval(input())
v = eval(input())
l = length()
print('The acceleration of {} M/s,the take-off speed is {} M/s,and the shortest take-off runway length is {} M'.format(name,v,l,'.2f'))
