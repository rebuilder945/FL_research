sName = input()
a = int(input())
v = int(input())
length = v*v/(2*a)
sText = "The acceleration of %s is %d M / s, the take-off speed is %d M / s, and the shortest take-off runway length is%.2f"% (sName,a,v,length)
print(sText)

