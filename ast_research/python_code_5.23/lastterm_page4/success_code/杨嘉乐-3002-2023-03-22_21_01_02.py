import numpy
ll=eval(input())
a=numpy.average(ll)
if a%1<1e-8:
    print(int(a))
else:
    print("%.2f",a)
