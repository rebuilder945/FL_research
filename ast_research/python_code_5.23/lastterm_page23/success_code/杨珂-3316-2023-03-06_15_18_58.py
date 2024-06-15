a=eval(input())
b=eval(input())
tmratio=a/(a+b)
tfratio=b/(a+b)
sText="The male students ratio is {:.2%},the female students ratio is {:.2%}".format(tmratio,tfratio)
print(sText)

