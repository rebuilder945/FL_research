strname=input()
englishword=[]
for i in range(97,123):
    englishword.append(chr(i))
for i in range(65,91):
    englishword.append(chr(i))
for i in strname:
    a=0
    if i in englishword:
        b=strname.count(i)
        a+=b
c=strname.count(' ')
for i in strname:
    d=0
    if i.isdigit():
        e=strname.count(i)
        d+=e
lenth=len(strname)
x=a+c+d
print(a,c,d,len(strname)-x)
