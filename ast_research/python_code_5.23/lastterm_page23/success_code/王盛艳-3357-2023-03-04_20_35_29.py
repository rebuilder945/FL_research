sName = str(input())
a = float(input())
v = int(input())
length  = (v**2)/(2*a)
sText = "The acceleration of %s is %.2fM / s, the take-off speed is %.2fM / s and the shortest take-off runway length is %.2fM."\
%(sName,a,v,(v**2/(2*a)))
print(sText)

