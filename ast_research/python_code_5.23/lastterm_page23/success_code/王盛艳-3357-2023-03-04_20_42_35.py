sName = str(input())
a = float(input())
v = float(input())
length  = (v**2)/(2*a)
sText = "The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M."\
%(sName,a,v,(v**2/(2*a)))
print(sText)

