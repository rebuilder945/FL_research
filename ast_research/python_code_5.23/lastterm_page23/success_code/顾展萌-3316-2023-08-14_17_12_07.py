def perman(a,b):
    c = a/(a+b)
    return c*100

m = eval(input())
n = eval(input())
male = perman(m,n)
female = perman(n,m)
print("The male students ratio is %.2f%%,the female students ratios is %.2f%%"%(male,female))

