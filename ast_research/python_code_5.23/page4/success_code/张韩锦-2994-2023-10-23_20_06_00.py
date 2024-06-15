lst=list(eval(input()))
n,m=eval(input())
lst2=[]
if n>=len(lst):
    print("error")
else:
    lst2.append(lst[n])
    del lst[n]
    print(lst+lst2*m)
