sName=input()
a=eval(input())
v=eval(input())
length=v*v/(a*2)
sText1="The acceleration of"
sText2="is"
sText3='the take-off speed is'
sText4='and the shortest take-off runway length is'
print(sText1,sName,sText2,"%.2f"%a,"M / s,",sText3,"%.2f"%v,"M / s,",sText4,'%.2f'%length,"M.")




