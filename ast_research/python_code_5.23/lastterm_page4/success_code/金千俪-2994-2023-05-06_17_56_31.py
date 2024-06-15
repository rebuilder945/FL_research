lst=list(eval(input()))
n,m=eval(input())
if n<=len(lst):
    for x in range(m):
        lst.insert(len(lst),lst[n])
    print(lst)
else:
    print("error")
