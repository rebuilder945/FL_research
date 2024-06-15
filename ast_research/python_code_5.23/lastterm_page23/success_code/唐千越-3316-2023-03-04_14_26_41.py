m=eval(input())
f=eval(input())
x="%"
a=m+f
mr="%.2f"%((m/a)*100)+x
fr="%.2f"%((f/a)*100)+x
sText="The male students ratio is %s, the female students ratio is %s" % (mr, fr)
print(sText)

