m=eval(input())
f=eval(input())
a=m+f
mr=round(float(m/a)*100)
fr=round(float(f/a)*100)
sText="The male students ratio is %.2f%，the female students ratio is %.2f%" % (mr, fr)
print(sText)
