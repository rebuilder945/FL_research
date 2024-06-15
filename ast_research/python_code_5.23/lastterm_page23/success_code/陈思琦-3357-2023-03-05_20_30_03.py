sName=input()
a=eval(input())
v=eval(input())
a=a+a
length=v*v/(a)
sText="The acceleration of %s is %.2f M/s,the take-off speed is %.2f,and the shortest take-off runway length is %.2f M." %(sName,a,v,length)
print(sText)
