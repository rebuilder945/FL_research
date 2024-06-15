lst=eval(input())
n,m=map(int,input().split(","))
lst2=[]
lst1=list(lst)
if n>=len(lst):
    print("error")
else:
     lst2.append(lst[n])
     lst2=lst2*m
     lst1.extend(lst2)
     print(lst1)

