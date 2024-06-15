lst=list(map(int,input().split(",")))
n,m=eval(input())
if n < len(lst):
    for i in range(0,m):
        ob=lst[n]
        lst.append(ob)
    print(lst)
else:
    print("error")
    
      

