lst = eval(input())
a,b = eval(input())
a = int(a)
b = int(b)
if n<len(lst) and m<len(lst):
    if n <m:
        del list[n:m]
        print(lst)
    else:
        del lst[m+1,n+1]
        print(lst)
else:
    print("error")
