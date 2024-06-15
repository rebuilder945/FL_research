mennumber = eval(input())
womennumber = eval(input())
number = mennumber + womennumber
mrate = '{:.2f}%'.format(mennumber/number*100)
wrate = '{:.2f}%'.format(womennumber/number*100)
print("The male students ratio is %s,the female students ratio is %s" % (mrate,wrate))

