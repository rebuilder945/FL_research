ls1=eval(input())
n,m=eval(input())
if m<len(ls1)and n<=m:
    for i in range(n,m):
        del ls1[i]
        print(ls1)
else:
    print("error")
