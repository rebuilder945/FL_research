name=input()
n=str(name)
a=input()
a1=float(a)
v=input()
v1=float(v)
length=(float(v)*float(v))/(2*float(a))               #前三行正确
stext = "The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, "\
    "and the shortest take-off runway length is %.2f M." %(n,a1,v1,length)
print(stext)
