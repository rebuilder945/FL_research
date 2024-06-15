lst=list(map(int,input().split(',')))
n,m=eval(input())
if n<=-len(lst) or n>=len(lst):
    print("error")
else:
    for i in range(m):
        lst.append(lst[n])
    print(lst)
