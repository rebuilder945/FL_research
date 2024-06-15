lst=list(input())
n,m=eval(input())
if -len(lst)-1<n<len(lst):
    for n in range(m):
        lst.append(lst[n])
    print(lst)
else:
    print("error")
