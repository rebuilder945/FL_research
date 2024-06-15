n = eval(input())
lst = [i for i in range(1, n+1)]
end = lst[n-1]
for i in range(n-1, -1, -1):
    lst[i] = lst[i-1]
lst[0] = end
print(lst)
