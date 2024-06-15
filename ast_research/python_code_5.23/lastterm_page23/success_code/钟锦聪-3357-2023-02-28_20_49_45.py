sName = input()
acceleration = eval(input())
speed = eval(input())
length = (speed*speed)/(2*acceleration)
sText="The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and "\
"the shortest take-off runway length is %.2f M."%(sName,acceleration,speed,length)
print(sText) 
