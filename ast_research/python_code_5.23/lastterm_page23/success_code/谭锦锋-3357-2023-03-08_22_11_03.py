name = input()
a = input()
v = input()
length1 = eval(v)*eval(v)/(2*eval(a))
length2 = "%.2f"%length1
print("The acceleration of",name,"is",a,"M/s,the take-off speed is",v,"M/s, and the shortest take-off runway length is",length2,"M.")
