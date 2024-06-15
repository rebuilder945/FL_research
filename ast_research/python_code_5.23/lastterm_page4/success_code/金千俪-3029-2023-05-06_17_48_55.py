lst=list(eval(input()))
n,m=eval(input())
if n<=len(lst):
    for x in range(m):
        lst.append(int(lst[n]))
    print(lst)
else:
    print("error")
