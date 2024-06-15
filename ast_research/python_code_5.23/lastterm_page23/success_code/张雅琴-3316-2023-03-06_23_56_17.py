a=eval(input())
b=eval(input())
c=a/(a+b)
d=b/(a+b)
sText1="The male students ratio is"
sText3="the female students ratio is"
sText2=","
print(sText1,'%.2f%%'%(c*100),sText2,sText3,"%.2f%%"%(d*100))
