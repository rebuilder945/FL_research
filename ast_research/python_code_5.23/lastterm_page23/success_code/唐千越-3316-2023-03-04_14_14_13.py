m=eval(input())
f=eval(input())
x="%"
a=m+f
mr="%.2f"%(round(float(m/a)*10000)/100)+x
fr="%.2f"%(round(float(f/a)*10000)/100)+x
print("The male students ratio is %s,the female students ratio is %s" % (mr, fr))

