l=eval(input())
n,m=eval(input())
if n>=0 and m<=len(l):
    del l[n:m]
    print(l)
else:
    print("error")
