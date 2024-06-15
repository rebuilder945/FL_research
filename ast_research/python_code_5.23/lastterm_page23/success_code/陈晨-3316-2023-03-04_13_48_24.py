m=eval(input())
f=eval(input())
t=m+f
x="%"
mb="%.2f"%(round(float(m/t)*10000)/100)+x
fb="%.2f"%(round(float(f/t)*10000)/100)+x
print("The male students ratio is %s,the female students ratio is %s"%(mb,fb))
