men=eval(input())
women=eval(input())
a=men+women
b=men/a
c=women/a
bb="%.2f%%" % (b*100)
cc="%.2f%%" % (c*100)
sText="The male students ratio is %s, the female students ratio is %s " % (bb,cc)
print(sText)

