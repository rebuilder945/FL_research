lst=list(map(int,input().split(",")))
n,m=eval(input())
lst2=lst[:]
if n < len(lst):
    for i in range(0,m):
        ob=lst[n]
        lst2.append(ob)
    print(lst2)
else:
    print("error")
    
      

