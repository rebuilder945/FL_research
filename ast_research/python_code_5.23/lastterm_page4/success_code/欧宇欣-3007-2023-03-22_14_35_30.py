sums=eval(input())
n,m=eval(input())
if n<len(sums) and m<len(sums):
    if n<=m:
        del sums[n:m]
        print(sums)
else:
    print("error")
