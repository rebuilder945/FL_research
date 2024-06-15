a=input.split('')
ls1=list(a)
n,m=eval(input())
ls2=list(a)
ls1[n]=ls2[m]
ls1[m]=ls2[n]
print(ls1)


