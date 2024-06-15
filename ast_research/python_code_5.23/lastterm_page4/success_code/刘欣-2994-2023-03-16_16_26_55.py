ls=list(eval(input()))
n,m=eval(input())
for i in range(len(ls)):
    if n>=len(ls) or n<-len(ls):
        print("error")
    else:
        ls.pop(n)
        repeat_n=ls.pop(n)*m
        ls.append(repeat_n)
        print(ls)
