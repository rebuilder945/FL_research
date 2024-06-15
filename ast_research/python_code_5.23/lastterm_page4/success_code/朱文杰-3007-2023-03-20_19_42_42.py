lst=eval(input())
n,m=eval(input())
if n<m:
    for x in range(n,m):
        if m<len(lst):
            del lst[x]
    else:
        print("error")
