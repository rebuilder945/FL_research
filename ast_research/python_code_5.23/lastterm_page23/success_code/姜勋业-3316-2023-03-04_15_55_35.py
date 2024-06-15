Sman=input()
Swomen=input()
sman=eval(Sman)
swomen=eval(Swomen)
a=sman+swomen
b=sman/a
c=swomen/a
b1='{:.2%}'.format(b)
c1='{:.2%}'.format(c)
stext="The male students ratio is % the female students ratio is %"(b1,c1)
print(stext)
