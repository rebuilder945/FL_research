list=eval(input())
n,m=eval(input().split(','))
if n<len(list) and m<len(list):
    if n<m:
        del list[n:m]
        print(list)
    else:
        del list[m+1:n+1]
        print(list)
else:
    print("error")


