lst=eval(input())
n,m=eval(input())
if n not in range(len(lst)):
    print("error")
else:
    del lst[n:m]
    print(lst)    
