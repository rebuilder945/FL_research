def iX(ia,ib):
    iG = ia/ib
    return iG
bn = eval(input())
gn = eval(input())
ib = gn+bn
print("The male students ratio is {:.2%},the female students ratio is {:.2%}".format(iX(bn,ib),iX(gn,ib)))
