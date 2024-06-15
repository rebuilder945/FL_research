a=eval(input())
b=eval(input())
sText1="The male students ratio is"
sText2="the female students ratio is"
print(sText1,'{:.2f}%'.format(a/a+b*100) , sText2,"{:.2f}%".format(b/a+b*100))
