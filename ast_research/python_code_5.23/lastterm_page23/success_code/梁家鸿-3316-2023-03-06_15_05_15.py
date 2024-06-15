def iX(ia,ib):
    iG = ia/ib
    return iG
bn = eval(input())
gn = eval(input())
ib = gn+bn
print("The male student ratio is {:.2%},the female student ratio is {:.2%}".format(iX(bn,ib),iX(gn,ib)))
