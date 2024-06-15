def perman(a,b):
    c = a/(a+b)
    return c

m = eval(input())
n = eval(input())
male = perman(m,n)*100
female = perman(n,m)*100
print("The male students ratio is %.2f% ,the female students ratios is %.2f%"%(male,female))

