lst=list(eval(input()))
m,n=eval(input())
a=lst[n]
if n>=len(lst):
    print("error")
else:
    for i in range(m):
        lst.append(a)
    print(lst)
