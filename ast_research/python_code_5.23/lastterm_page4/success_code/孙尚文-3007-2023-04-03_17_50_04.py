lst=eval(input())
n,m=eval(input())
if n<-len(lst) or n>=len(lst) or m<-len(lst) or m>=len(lst) or n>m:
    print("error")
else:
    print(lst[:n]+lst[m:])    
