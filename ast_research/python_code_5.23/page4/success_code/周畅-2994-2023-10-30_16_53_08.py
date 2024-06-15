lst=list(map(int,(input()).split(",")))
n,m=eval(input())
lst2=[]
if(n+1)<=len(lst):
    for x in range(m):
        lst2.append(lst[n])
    lst=lst+lst2
    print(lst)
else:
    print("error")
