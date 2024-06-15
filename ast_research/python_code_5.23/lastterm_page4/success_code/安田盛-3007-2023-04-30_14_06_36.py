lst=eval(input())
n,m=eval(input())
if n<m<=len(lst):
    for i in range(m-n):
        del lst[n]
    print(lst)
else:
    print("error")


