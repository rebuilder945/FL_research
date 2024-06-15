def swap_elements(lst, n, m):
    lst[n], lst[m] = lst[m], lst[n]
    return lst
lst=list(input().split())
x=list(input().split())
n=int(x[0])
m=int(x[1])
lst1=swap_elements(lst, n, m)
print(lst1)
