sname=input()
a=eval(input())
v=eval(input())
lengh=v*v/(2*a)
text=('The acceleration of ',sname, 'is' ,a,'M / s, the take-off speed is',v,' M / s, and the shortest take-off runway length is','%,2f'%lengh ,'M')
print(text)


