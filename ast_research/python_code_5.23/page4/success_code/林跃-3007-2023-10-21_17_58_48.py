lst=eval(input())
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    del lst[n:m]
print(lst)
 
