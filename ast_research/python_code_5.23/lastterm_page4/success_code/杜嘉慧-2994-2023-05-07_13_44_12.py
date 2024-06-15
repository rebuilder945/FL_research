lst=[int(x)for x in input().split(',')]
n,m=[int(x)for x in input().split(',')]
a=lst[n]
if n>=len(lst):
    print("error")
else:
    lst+=[a]*m
    print(lst)
