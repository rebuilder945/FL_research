lst=eval(input())
n,m=[int(x)for x in input().split(',')]
if (n>=0 and n<len(lst) and m>=0 and m<len(lst)):
    new=lst[:n]+lst[m:]
    print(new)
else:
    print("error")
