def length():
    l = v*v/(2*a)
    return l
name = input()
a = eval(input())
v = eval(input())
l = eval(length())
print("%.2f"%'The acceleration of %s M/s,the take-off speed is %s M/s,and the shortest take-off runway length is %s M'%name,a,v,l)
