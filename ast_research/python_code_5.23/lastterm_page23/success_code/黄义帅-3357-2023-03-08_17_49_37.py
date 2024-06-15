name=input("Enter the plane's name")
a=eval(input("Enter the acceleration"))
v=eval(input("Enter the speed"))
length=v*v/(2*a)
print("The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M."%(name,a,v,length))

