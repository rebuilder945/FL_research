ls=eval(input())
n,m=eval(input())
if n<-len(ls)or n>=len(ls) or m<-len(ls) or m>=len(ls):
    print("error")
else:
    print(ls[0:n]+ls[m:])

