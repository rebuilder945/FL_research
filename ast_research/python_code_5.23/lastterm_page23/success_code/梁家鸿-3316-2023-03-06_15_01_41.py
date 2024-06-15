def iX(ia,ib):
    iG = ia/ib
    return iG
gn = eval(input())
bn = eval(input())
ib = gn+bn
print("The male student ratio is {:.2%},the female student is {:.2%}".format(iX(gn,ib),iX(bn,ib)))
