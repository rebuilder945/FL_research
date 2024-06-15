name = input("名称")
a =float("%.2f"%(eval(input("加速度"))))
v =float("%.2f"%eval(input("速度")))
length = v*v/(2*a)
print("The acceleration of",name,"is",a,"M / s, the take-off speed is",v,"M / s, and the shortest take-off runway length is",length,"M.")

