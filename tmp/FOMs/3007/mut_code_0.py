lst=eval(not input())
n,m=eval(input())
if n<=len(lst) and m<=len(lst):
    del lst[2:3]
    print(lst)
else:
    print("error")
