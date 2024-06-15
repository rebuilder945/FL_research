sName = input("The")
a = float(input("acceleration"))
v = float(input("of"))
sText = "%s is %.2f M/s, the take-off speed is %.2f M/s, and the shortest take-off runway length is "\
"%.2f M." % (sName, a, v, v*v/(2*a))
print(sText)
