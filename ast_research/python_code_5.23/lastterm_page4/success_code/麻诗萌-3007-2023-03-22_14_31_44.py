lst=eval(input())
n,m=eval(input())
if m > len(lst) :
    print("error")
else :
    del lst[n:m]
    print(lst)    
