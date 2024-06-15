def select_and_append(lst,m,n):
    if abs(n)>len(lst):
        return "error"
    else:
        selected=lst[n-1]
        for i in range(m):
            lst.append(selected)
        return (lst)
lst=list(eval(input()))
n,m=eval(input())
k=select_and_append(lst,n,m)
print(k)
