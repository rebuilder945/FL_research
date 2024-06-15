lst=list(eval(input()))
n,m=eval(input())
if n>len(lst)+1:
    print("error")
else:
    for i in range(m):
        lst.append(lst[n])
print(lst)

