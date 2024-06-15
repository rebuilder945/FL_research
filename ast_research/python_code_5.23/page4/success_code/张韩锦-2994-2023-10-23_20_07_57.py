lst=list(eval(input()))
n,m=eval(input())
lst2=[]
if n>=len(lst) or n<-1*len(lst):
    print("error")
else:
    lst2.append(lst[n])
    print(lst+lst2*m)
