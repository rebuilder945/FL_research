name = input()
a1 = input()
a2 = "%.2f"%eval(a1)
v1 = input()
v2 = "%.2f"%eval(v1)
length1 = eval(v1)*eval(v1)/(2*eval(a1))
length2 = "%.2f"%length1
print("The acceleration of",name,"is",a2,"M / s, the take-off speed is",v2,"M / s, and the shortest take-off runway length is",length2,"M.")
