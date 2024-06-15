ls1=eval(input())
n,m=eval(input())
if m<=len(ls1):
    del ls1[n:m]
    print(ls1)
else:
    print("error")
