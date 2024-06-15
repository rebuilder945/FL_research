strname=input()
englishword=[]
for i in range(97,123):
    englishword.append(chr(i))
a=0
for i in strname:
    if i in englishword:
        b=strname.count(i)
        a+=b
c=strname.count(' ')
for i in strname:
    d=0
    if type(i)==int or type(i)==float:
        e=strname.count(i)
        d+=e
lenth=len(strname)
x=a+c+d
print(a,c,d,len(strname)-x)
