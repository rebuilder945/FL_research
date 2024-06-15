m=eval(input())
f=eval(input())
t=m+f
x="%"
mb=str(round(float(m/t)*10000)/100)+x
fb=str(round(float(f/t)*10000)/100)+x
print("The male students ratio is %s,the female students ratio is %s"%(mb,fb))
