lst=eval(input())
n,m=eval(input())
if m<=len(lst) and n<= len(lst) : 
    for i in range(m-n):
        del lst[n+i]
    print(lst)
else:
    print(False)
