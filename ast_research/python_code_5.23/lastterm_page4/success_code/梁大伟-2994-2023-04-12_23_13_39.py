lst=list(map(int,input().split(',')))
ls=[]
for s in range(len(lst)):
    ls.append(lst[s])
n,m=eval(input())
if n<=-len(lst) or n>=len(lst):
    print("error")
else:
    for i in range(m):
        ls.append(lst[n])
    print(ls)

