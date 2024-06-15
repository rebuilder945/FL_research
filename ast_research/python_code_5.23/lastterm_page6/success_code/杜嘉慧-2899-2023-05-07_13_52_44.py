lst=[int(x)for x in input().split(',')]
n,m=[int(x)for x in input().split(',')]
if n>=len(lst):
    print("error")
else:
    a=lst[n]
    lst+=[a]*m
    print(lst)
