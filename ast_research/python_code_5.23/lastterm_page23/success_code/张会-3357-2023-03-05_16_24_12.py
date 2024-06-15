sName = "B350"
a = 3.572
v = 60
sText ="The acceleration of %s is %.3f M/s, the take-off speed is %d M/s, and the shortest take-off runway length is "\
"%.2f M." % (sName, a, v, v*v/2/a)
print(sText)
