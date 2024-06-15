n=list(map(int,input().split(",")))
x,y=eval(input())
if x >=len(n) or x<-len(n):
    print("error")
else:
    c=[n[x]]*y
    print(n+c)
    








