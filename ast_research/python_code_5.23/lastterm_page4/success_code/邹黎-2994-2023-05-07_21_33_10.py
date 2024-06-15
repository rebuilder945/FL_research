lst=list(input().split(","))
a,b=eval(input())
if a>=len(lst) or a<(-len(lst)):
    print("error")
else:
    chu=lst[a]
    for x in range(1,b+1,1):
        lst.append(chu)
    print(lst)


