list=list(eval(input()))
n,m=map(int,input().split(","))
if n<len(list) and m<len(list):
    if n<m:
        del list[n:m]
        print(list)
    else:
        print(list)
else:
    print("error")
