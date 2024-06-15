biao=eval(input())
n,m=eval(input())
if n<=len(biao) and m<=len(biao):
    del biao[n:m]
    print(biao)
else:
    print("error")
