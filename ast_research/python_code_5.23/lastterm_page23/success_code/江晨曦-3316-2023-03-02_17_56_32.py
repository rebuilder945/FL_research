# a=input()
# print(a.upper())

# sName=input()
# a=float(input())
# v=eval(input())
# length=v*v/(2*a)
# print("The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M."%(sName,a,v,length))

iMan = eval(input())
iWoman = eval(input())
iTotal = iMan + iWoman
p1 = iMan/iTotal
p2 = iWoman/iTotal
print('The male students ratio is {:.2%},the female students ratio is {:.2%}'.format(p1,p2))
