lst=eval(input())
n,m=eval(input())
if m>=n>len(lst):
    print("error")
elif n<=m<=len(lst):
    del lst[n:m]
    print(lst)




        







