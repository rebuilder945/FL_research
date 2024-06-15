lst=eval(input())
n,m=eval(input())
lens=len(lst)
if n<lens and m<lens :
    del lst[n:m]
    print(lst)
else:
    print("error")
