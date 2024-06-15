from distutils.log import error
lst=eval(input())
n,m=eval(input())
if n not in range(len()) or m not in range(len(lst)):
    print("erorr")
else:
    del lst[n:m]
    print(lst)
