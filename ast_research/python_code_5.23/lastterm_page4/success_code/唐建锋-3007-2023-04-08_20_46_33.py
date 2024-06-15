lst=eval(input())
n,m=eval(input())
if(n<-len(lst) or n>=len(lst) or m<-len(lst) or m>= len(lst)):
    print("error")
else:
    print(lst[:n]+lst[m:])
