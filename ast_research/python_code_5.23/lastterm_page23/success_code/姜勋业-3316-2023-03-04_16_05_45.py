Sman=input()
Swomen=input()
sman=float(Sman)
swomen=float(Swomen)
a=sman+swomen
b=sman/a
c=swomen/a
b1='{:.2%}'.format(b)
c1='{:.2%}'.format(c)
b2=str(b1)
c2=str(c1)
stext="The male students ratio is %s the female students ratio is %s "(b2,c2)
print(stext)
