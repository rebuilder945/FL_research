from distutils.log import erorr
lst=eval(input())
n,m=eval(input())
if n not in range(len(lst)) or m not in range(len(lst)):
    print("erorr")
else:
    del lst[n:m]
    print(lst)
