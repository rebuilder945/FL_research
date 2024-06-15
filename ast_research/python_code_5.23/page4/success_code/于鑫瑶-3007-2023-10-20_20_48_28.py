ls1=input()
n,m=eval(input())
if n in ls1:
    if m in ls1:
        if n<m:
           del ls1[n:m]
           print(ls1)
        else:
            del ls1[m:n]
            print(ls1)
    else:
        print("error")
else:
    print("error")
