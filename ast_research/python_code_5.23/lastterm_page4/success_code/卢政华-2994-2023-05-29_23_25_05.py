lst=list(eval(input()))
n,m=eval(input())
lst2=[]
if n <len(lst):
    lst2.append(lst[n]*m)
    print(lst+lst2)
else:
    print("error")
