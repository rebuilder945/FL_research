n = eval(input())
lst = list(range(1,n+1))
a = lst[0]
for i in range(n-1) :
    lst[i] = lst[i+1]
lst[-1] = a
print(lst)
