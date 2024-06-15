from distutils.log import error
ls1=eval(input())
n,m=eval(input())
if n not in range(len(ls1)) or m not in range(len(ls1)):
    print("error")
else:
    del ls1[n:m]
    print(ls1)
