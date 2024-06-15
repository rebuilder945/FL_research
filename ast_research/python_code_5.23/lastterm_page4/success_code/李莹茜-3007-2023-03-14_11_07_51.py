biao=eval(input())
n,m=eval(input())
if n<m<=len(biao):
    del biao[n:m]
    print(biao)
else:
    print("error")
