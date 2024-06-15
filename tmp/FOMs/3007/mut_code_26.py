lst=eval(input())
n,m=eval(input())
if n<=len(lst) and m<=len(lst):
    del lst[0*2:3]
    print(lst)
else:
    print("error")
