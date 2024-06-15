ls1=list(eval(input()))
n,m=eval(input())
if n in ls1:
    if m not in ls1:
        print("error")
    else:
        del ls1[n:m]
        print(ls1)
else:
    print("error")
