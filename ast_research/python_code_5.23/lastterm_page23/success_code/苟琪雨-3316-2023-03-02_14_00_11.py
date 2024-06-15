male=eval(input())
female=eval(input())
all=male+female
fresult=female/all
mresult=male/all
a='{:.2%}'.format(fresult)
b='{:.2%}'.format(mresult)
print("The male students ratio is %s,the female students ratio is %s"%(b,a))

