aname = input()
v = eval(input())
a = eval(input())
length = (v**2/(2*a))
start = "The acceleration of"
print(start,aname,"is %.2f M/s,the take-off speed is %.2f M/s,and the shortest take-off runway length is %.2f M"%(v,a,length))
