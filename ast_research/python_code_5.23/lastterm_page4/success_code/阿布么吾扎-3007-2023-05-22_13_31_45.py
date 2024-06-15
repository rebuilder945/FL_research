lst=eval(input())
n,m=eval(input())
a=len(lst)
if m>=a or m<-a or n>=a or n<-a:
    print('error')
else:
    print(lst[0:n]+lst[m::])
