sName = input()
jiasudu = eval(input())
sudu = eval(input())
sText = "The acceleration of %s is %.2f M/s, the take-off speed is %.2f M/s, and the shortest take-off runway length is "\
"%.2f M." % (sName, jiasudu, sudu, sudu*sudu/(2*jiasudu))
print(sText)
