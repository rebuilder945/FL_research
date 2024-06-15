lst=eval(input())
n,m=map(int,input().split(","))
lst2=[]
if n>=len(lst):
    print("error")
else:
    for i in range(len(lst)):
        if i==n:
            lst2.append(lst[i])
            lst2=lst2*m
            lst2[0:0]=lst
            print(lst2)
