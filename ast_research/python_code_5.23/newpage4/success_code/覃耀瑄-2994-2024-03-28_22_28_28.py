list1=eval(input())
n,m=map(int,input().spilt())
list2=[]
while len(list2)<m:
    list2.append(list1[n])
if len(list1)>n:
    list1=list1+list2
    print(list1)
else:
    print("error")

