def length(vSpeed,aAcceleration):
    length = vSpeed*vSpeed/(2*aAcceleration)
    return length
sName = input()
vSpeed = eval(input())
aAcceleration = eval(input())
print("The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M."%(sName,vSpeed,aAcceleration,length))
