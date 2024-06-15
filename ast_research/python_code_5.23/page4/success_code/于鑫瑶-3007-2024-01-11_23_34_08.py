ls1=eval(input())
n,m=eval(input())
if m<=len(ls1):
    del ls1[n:m]
    print(ls1)
elif n>=m or m>=len(ls1):
    print("error")
