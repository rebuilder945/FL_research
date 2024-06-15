def iX(ia,ib):
    iX = ia/ib
gn = input()
bn = input()
ib = gn+bn
iF = eval(print('persent:{:.2%'.format(iX(gn,ib))))
iM = eval(print('persent:{:.2%'.format(iX(bn,ib))))
print("The male student ratio is",iM,",the female student is",iF)
