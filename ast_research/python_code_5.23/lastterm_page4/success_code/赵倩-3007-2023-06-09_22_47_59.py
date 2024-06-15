lst=eval(input())
n,m=eval(input())
if m>=n>len(lst)-1:
    print("error")
elif n<=m<=len(lst)-1:
    del lst[n:m]
    print(lst)




        







